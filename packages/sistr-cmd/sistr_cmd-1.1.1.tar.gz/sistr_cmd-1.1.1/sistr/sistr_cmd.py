#!/usr/bin/env python
from __future__ import print_function

import argparse
from collections import Counter
from datetime import datetime
import logging
import re, sys
import os, pycurl, tarfile, zipfile, gzip, shutil
from pkg_resources import resource_filename


from sistr.version import __version__
from sistr.src.blast_wrapper import BlastRunner
from sistr.src.cgmlst import run_cgmlst
from sistr.src.logger import init_console_logger
from sistr.src.qc import qc
from sistr.src.serovar_prediction import SerovarPredictor, overall_serovar_call, serovar_table, SISTR_DB_URL, SISTR_DATA_DIR


def init_parser():
    prog_desc = '''
SISTR (Salmonella In Silico Typing Resource) Command-line Tool
==============================================================
Serovar predictions from whole-genome sequence assemblies by determination of antigen gene and cgMLST gene alleles using BLAST.

Note about using the "--use-full-cgmlst-db" flag:
    The "centroid" allele database is ~10% the size of the full set so analysis is much quicker with the "centroid" vs "full" set of alleles. Results between 2 cgMLST allele sets should not differ.

If you find this program useful in your research, please cite as:

The Salmonella In Silico Typing Resource (SISTR): an open web-accessible tool for rapidly typing and subtyping draft Salmonella genome assemblies.
Catherine Yoshida, Peter Kruczkiewicz, Chad R. Laing, Erika J. Lingohr, Victor P.J. Gannon, John H.E. Nash, Eduardo N. Taboada.
PLoS ONE 11(1): e0147101. doi: 10.1371/journal.pone.0147101
'''

    parser = argparse.ArgumentParser(prog='sistr_cmd',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=prog_desc)

    parser.add_argument('fastas',
                        metavar='F',
                        nargs='*',
                        help='Input genome FASTA file')
    parser.add_argument('-i',
                        '--input-fasta-genome-name',
                        nargs=2,
                        metavar=('fasta_path', 'genome_name'),
                        action='append',
                        help='fasta file path to genome name pair')
    parser.add_argument('-f',
                        '--output-format',
                        default='json',
                        help='Output format (json, csv, pickle)')
    parser.add_argument('-o',
                        '--output-prediction',
                        help='SISTR serovar prediction output path')
    parser.add_argument('-M',
                        '--more-results',
                        action='count',
                        default=0,
                        help='Output more detailed results (-M) and all antigen search blastn results (-MM)')
    parser.add_argument('-p',
                        '--cgmlst-profiles',
                        help='Output CSV file destination for cgMLST allelic profiles')
    parser.add_argument('-n',
                        '--novel-alleles',
                        help='Output FASTA file destination of novel cgMLST alleles from input genomes')
    parser.add_argument('-a',
                        '--alleles-output',
                        help='Output path of allele sequences and info to JSON')
    parser.add_argument('-T',
                        '--tmp-dir',
                        default='/tmp',
                        help='Base temporary working directory for intermediate analysis files.')
    parser.add_argument('-K',
                        '--keep-tmp',
                        action='store_true',
                        help='Keep temporary analysis files.')
    parser.add_argument('--use-full-cgmlst-db',
                        action='store_true',
                        help='Use the full set of cgMLST alleles which can include highly similar alleles. By default the smaller "centroid" alleles or representative alleles are used for each marker. ')
    parser.add_argument('--no-cgmlst',
                        action='store_true',
                        help='Do not run cgMLST serovar prediction')
    parser.add_argument('-m', '--run-mash',
                        action='store_true',
                        help='Determine Mash MinHash genomic distances to Salmonella genomes with trusted serovar designations. Mash binary must be in accessible via $PATH (e.g. /usr/bin).')
    parser.add_argument('--qc',
                        action='store_true',
                        help='Perform basic QC to provide level of confidence in serovar prediction results.')
    parser.add_argument('-t', '--threads',
                        type=int,
                        default=1,
                        help='Number of parallel threads to run sistr_cmd analysis.')
    parser.add_argument('-v',
                        '--verbose',
                        action='count',
                        default=0,
                        help='Logging verbosity level (-v == show warnings; -vvv == show debug info)')
    parser.add_argument('-V', '--version', action='version', version='%(prog)s {}'.format(__version__))
    return parser


def run_mash(input_fasta):
    from sistr.src.mash import mash_dist_trusted, mash_output_to_pandas_df, mash_subspeciation

    mash_out = mash_dist_trusted(input_fasta)
    df_mash = mash_output_to_pandas_df(mash_out)
    if df_mash.empty:
        logging.error('Could not perform Mash subspeciation!')
        mash_result_dict = {
            'mash_genome': '',
            'mash_serovar': '',
            'mash_distance': 1.0,
            'mash_match': 0,
            'mash_subspecies': '',
            'mash_top_5': {},
        }
        return mash_result_dict
    df_mash_top_5 = df_mash[['ref', 'dist', 'n_match', 'serovar']].head(n=5)
    logging.debug('Mash top 5 results:\n{}\n'.format(df_mash_top_5))
    mash_spp_tuple = mash_subspeciation(df_mash)
    spp = None
    if mash_spp_tuple is not None:
        spp, spp_dict, spp_counter = mash_spp_tuple
        logging.info('Mash spp %s (dist=%s; counter=%s)', spp, spp_dict, spp_counter)

    else:
        logging.error('Could not perform Mash subspeciation!')

    for idx, row in df_mash_top_5.iterrows():
        mash_genome = row['ref']
        mash_serovar = row['serovar']
        mash_distance = row['dist']
        mash_match = row['n_match']

        log_msg = 'Top serovar by Mash: "{}" with dist={}, # matching sketches={}, matching genome={}'
        logging.info(log_msg.format(mash_serovar, mash_distance, mash_match, mash_genome))

        mash_result_dict = {
            'mash_genome': mash_genome,
            'mash_serovar': mash_serovar,
            'mash_distance': mash_distance,
            'mash_match': mash_match,
            'mash_subspecies': spp,
            'mash_top_5': df_mash_top_5.to_dict(),
        }
        return mash_result_dict


def merge_mash_prediction(prediction, mash_prediction):
    for k in mash_prediction:
        prediction.__dict__[k] = mash_prediction[k]
    return prediction


def merge_cgmlst_prediction(serovar_prediction, cgmlst_prediction):
    serovar_prediction.cgmlst_distance = cgmlst_prediction['distance']
    serovar_prediction.cgmlst_genome_match = cgmlst_prediction['genome_match']
    serovar_prediction.serovar_cgmlst = cgmlst_prediction['serovar']
    if 'found_loci' in cgmlst_prediction:
        serovar_prediction.cgmlst_found_loci = cgmlst_prediction['found_loci']
    else:
        serovar_prediction.cgmlst_found_loci = 0
    serovar_prediction.cgmlst_matching_alleles = cgmlst_prediction['matching_alleles']
    serovar_prediction.cgmlst_subspecies = cgmlst_prediction['subspecies']
    serovar_prediction.cgmlst_ST = cgmlst_prediction['cgmlst330_ST']
    return serovar_prediction



def infer_o_antigen(prediction):
    df_serovar = serovar_table()
    if '|' in prediction.serovar:
        prediction.o_antigen = '-'
    else:
        predicted_serovars = [prediction.serovar]
        series_o_antigens = df_serovar.O_antigen[df_serovar.Serovar.isin(predicted_serovars)]
        if series_o_antigens.size == 0:
            prediction.o_antigen = '-'
        else:
            counter_o_antigens = Counter(series_o_antigens)
            prediction.o_antigen = counter_o_antigens.most_common(1)[0][0]

def download_to_file(url,file):
    with open(file, 'wb') as f:
        c = pycurl.Curl()
        # Redirects to https://www.python.org/.
        c.setopt(c.URL, url)
        # Follow redirect.
        c.setopt(c.FOLLOWLOCATION, True)
        c.setopt(c.WRITEDATA, f)
        c.perform()
        c.close()

def extract(fname,outdir):
    if (fname.endswith("tar.gz")):
        tar = tarfile.open(fname, "r:gz")
        tar.extractall(outdir)
        tar.close()
    elif (fname.endswith("tar")):
        tar = tarfile.open(fname, "r:")
        tar.extractall(outdir)
        tar.close()
    elif(fname.endswith("zip")):
        zip_ref = zipfile.ZipFile(fname, 'r')
        zip_ref.extractall(outdir)
        zip_ref.close()
    elif(fname.endswith("gz")):
        outfile = os.path.join(outdir,fname.replace('.gz',''))
        with gzip.open(fname, 'rb') as f_in:
            with open(outfile, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
            f_in.close()
            f_out.close()
            os.remove(fname)

def setup_sistr_dbs():
    tmp_file = resource_filename('sistr', 'data.tar.gz')
    logging.info("Downloading needed SISTR databases from: {}".format(SISTR_DB_URL))
    download_to_file(SISTR_DB_URL, tmp_file)
    if os.path.isdir(resource_filename('sistr', 'data/')):
        shutil.rmtree(resource_filename('sistr', 'data/'))
        os.mkdir(resource_filename('sistr', 'data/'))
    if (not os.path.isfile(tmp_file)):
        logging.error('Downloading databases failed, please check your internet connection and retry')
        sys.exit(-1)
    else:
        logging.info('Downloading databases successful')
        f = open(resource_filename('sistr', 'dbstatus.txt'),'w')
        f.write("DB downloaded on : {} from {}".format(datetime.today().strftime('%Y-%m-%d'),SISTR_DB_URL))
        f.close()

    extract(tmp_file, resource_filename('sistr', ''))
    os.remove(tmp_file)



def sistr_predict(input_fasta, genome_name, tmp_dir, keep_tmp, args):
    blast_runner = None
    try:
        assert os.path.exists(input_fasta), "Input fasta file '%s' must exist!" % input_fasta
        if genome_name is None or genome_name == '':
            genome_name = genome_name_from_fasta_path(input_fasta)
        dtnow = datetime.now()
        genome_name_no_spaces = re.sub(r'\W', '_', genome_name)
        genome_tmp_dir = os.path.join(tmp_dir, dtnow.strftime("%Y%m%d%H%M%S") + '-' + 'SISTR' + '-' + genome_name_no_spaces)
        blast_runner = BlastRunner(input_fasta, genome_tmp_dir)
        logging.info('Initializing temporary analysis directory "%s" and preparing for BLAST searching.', genome_tmp_dir)
        blast_runner.prep_blast()
        logging.info('Temporary FASTA file copied to %s', blast_runner.tmp_fasta_path)
        spp = None
        mash_prediction = None
        if args.run_mash:
            mash_prediction = run_mash(input_fasta)
            spp = mash_prediction['mash_subspecies']

        cgmlst_prediction = None
        cgmlst_results = None
        if not args.no_cgmlst:
            cgmlst_prediction, cgmlst_results = run_cgmlst(blast_runner, full=args.use_full_cgmlst_db)
            spp = cgmlst_prediction['subspecies']

        serovar_predictor = SerovarPredictor(blast_runner, spp)
        serovar_predictor.predict_serovar_from_antigen_blast()

        prediction = serovar_predictor.get_serovar_prediction()
        prediction.genome = genome_name
        prediction.fasta_filepath = os.path.abspath(input_fasta)
        if cgmlst_prediction:
            merge_cgmlst_prediction(prediction, cgmlst_prediction)
        if mash_prediction:
            merge_mash_prediction(prediction, mash_prediction)
        overall_serovar_call(prediction, serovar_predictor)
        infer_o_antigen(prediction)
        logging.info('%s | Antigen gene BLAST serovar prediction: "%s" serogroup=%s %s:%s:%s',
                     genome_name,
                     prediction.serovar_antigen,
                     prediction.serogroup,
                     prediction.o_antigen,
                     prediction.h1,
                     prediction.h2)
        logging.info('%s | Subspecies prediction: %s',
                     genome_name,
                     spp)
        logging.info('%s | Overall serovar prediction: %s',
                     genome_name,
                     prediction.serovar)
        if args.qc:
            qc_status, qc_msgs = qc(blast_runner.tmp_fasta_path, cgmlst_results, prediction)
            prediction.qc_status = qc_status
            prediction.qc_messages = ' | '.join(qc_msgs)
    finally:
        if not keep_tmp:
            logging.info('Deleting temporary working directory at %s', blast_runner.tmp_work_dir)
            blast_runner.cleanup()
        else:
            logging.info('Keeping temp dir at %s', blast_runner.tmp_work_dir)
    return prediction, cgmlst_results


def genome_name_from_fasta_path(fasta_path):
    """Extract genome name from fasta filename

    Get the filename without directory and remove the file extension.

    Example:
        With fasta file path ``/path/to/genome_1.fasta``::

            fasta_path = '/path/to/genome_1.fasta'
            genome_name = genome_name_from_fasta_path(fasta_path)
            print(genome_name)
            # => "genome_1"

    Args:
        fasta_path (str): fasta file path

    Returns:
        str: genome name
    """
    filename = os.path.basename(fasta_path)
    return re.sub(r'(\.fa$)|(\.fas$)|(\.fasta$)|(\.fna$)|(\.\w{1,}$)', '', filename)


def write_cgmlst_profiles(fastas, cgmlst_results, output_path):
    genome_marker_cgmlst_result = {}
    for genome, res in zip(fastas, cgmlst_results):
        tmp = {}
        for marker, res_dict in res.items():
            aname = res_dict['name']
            tmp[marker] = int(aname) if aname is not None else None
        genome_marker_cgmlst_result[genome] = tmp
    import pandas as pd
    df = pd.DataFrame(genome_marker_cgmlst_result).transpose()
    df.to_csv(output_path, float_format='%.0f')


def write_cgmlst_results_json(input_fastas, cgmlst_results, output_path):
    import json
    with open(output_path, 'w') as fout:
        json.dump({x:y for x,y in zip(input_fastas, cgmlst_results)}, fout)


def write_novel_alleles(cgmlst_results, output_path):
    count = 0
    with open(output_path, 'w') as fout:
        for x in cgmlst_results:
            for marker, res in x.items():
                name = res['name']
                seq = res['seq']
                br = res['blast_result']
                if br is not None and isinstance(br, dict):
                    trunc = br['trunc']
                    if not trunc:
                        fout.write('>{}|{}\n{}\n'.format(marker, name, seq))
                        count += 1
    return count


def main():

    parser = init_parser()
    args = parser.parse_args()
    init_console_logger(args.verbose)
    logging.info('Running sistr_cmd {}'.format(__version__))
    if not os.path.isfile(resource_filename('sistr', 'dbstatus.txt')):
        setup_sistr_dbs()
    input_fastas = args.fastas
    paths_names = args.input_fasta_genome_name
    if len(input_fastas) == 0 and (paths_names is None or len(paths_names) == 0):
        logging.error('No FASTA files specified!')
        parser.print_help()
        sys.exit(-1)
    if paths_names is None:
        genome_names = [genome_name_from_fasta_path(x) for x in input_fastas]
    else:
        if len(input_fastas) == 0 and len(paths_names) > 0:
            input_fastas = [x for x,y in paths_names]
            genome_names = [y for x,y in paths_names]
        elif len(input_fastas) > 0 and len(paths_names) > 0:
            tmp = input_fastas
            input_fastas = [x for x,y in paths_names] + tmp
            genome_names = [y for x,y in paths_names] + [genome_name_from_fasta_path(x) for x in tmp]
        else:
            logging.error('Unhandled fasta input args: input_fastas="{}" | input_fasta_genome_name="{}"'.format(
                input_fastas,
                paths_names))
            parser.print_help()
            sys.exit(-1)

    tmp_dir = args.tmp_dir
    keep_tmp = args.keep_tmp
    output_format = args.output_format
    output_path = args.output_prediction


    n_threads = args.threads
    if n_threads == 1:
        logging.info('Serial single threaded run mode on %s genomes', len(input_fastas))
        outputs = [sistr_predict(input_fasta, genome_name, tmp_dir, keep_tmp, args) for input_fasta, genome_name in zip(input_fastas, genome_names)]
    else:
        from multiprocessing import Pool
        logging.info('Initializing thread pool with %s threads', n_threads)
        pool = Pool(processes=n_threads)
        logging.info('Running SISTR analysis asynchronously on %s genomes', len(input_fastas))
        res = [pool.apply_async(sistr_predict, (input_fasta, genome_name, tmp_dir, keep_tmp, args)) for input_fasta, genome_name in zip(input_fastas, genome_names)]

        logging.info('Getting SISTR analysis results')
        outputs = [x.get() for x in res]

    prediction_outputs = [x for x,y in outputs]

    cgmlst_results = [y for x,y in outputs]

    if output_path:
        from sistr.src.writers import write
        logging.info('Writing results with %s verbosity',
                     args.more_results)
        write(output_path, output_format, prediction_outputs, more_results=args.more_results)
    else:
        import json
        from sistr.src.writers import to_dict
        logging.warning('No prediction results output file written! Writing results summary to stdout as JSON')
        exclude_keys_in_output = {'blast_results', 'sseq'}
        if args.more_results >= 2:
            exclude_keys_in_output.remove('blast_results')
            exclude_keys_in_output.remove('sseq')
        elif args.more_results == 1:
            exclude_keys_in_output.remove('sseq')
        outs = [to_dict(x, 0, exclude_keys=exclude_keys_in_output) for x in prediction_outputs]
        print(json.dumps(outs))
    if args.cgmlst_profiles:
        write_cgmlst_profiles(genome_names, cgmlst_results, args.cgmlst_profiles)
        logging.info('cgMLST allelic profiles written to %s', args.cgmlst_profiles)
    if args.alleles_output:
        write_cgmlst_results_json(genome_names, cgmlst_results, args.alleles_output)
        logging.info('JSON of allele data written to %s for %s cgMLST allele results', args.alleles_output, len(cgmlst_results))
    if args.novel_alleles:
        count = write_novel_alleles(cgmlst_results, args.novel_alleles)
        logging.info('Wrote %s alleles to %s', count, args.novel_alleles)




if __name__ == '__main__':
    main()


