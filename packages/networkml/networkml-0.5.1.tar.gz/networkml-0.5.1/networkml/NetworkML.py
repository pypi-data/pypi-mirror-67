import argparse
import datetime
import logging
import os
import time

import humanize

from networkml import __version__
from networkml.algorithms.host_footprint import HostFootprint
from networkml.featurizers.csv_to_features import CSVToFeatures
from networkml.parsers.pcap_to_csv import PCAPToCSV
from networkml.helpers.results_output import ResultsOutput


class NetworkML():

    def __init__(self, raw_args=None):
        self.logger = logging.getLogger(__name__)
        self.main(raw_args=raw_args)

    @staticmethod
    def parse_args(raw_args=None):
        parser = argparse.ArgumentParser()
        parser.add_argument('path', help='path to a single pcap file, or a directory of pcaps to parse', default='/pcaps')
        parser.add_argument('--algorithm', '-a', choices=[
                            'host_footprint'], default='host_footprint', help='choose which algorithm to use (default=host_footprint)')
        parser.add_argument('--engine', '-e', choices=['pyshark', 'tshark', 'host'],
                            default='tshark', help='engine to use to process the PCAP file (default=tshark)')
        parser.add_argument('--first_stage', '-f', choices=['parser', 'featurizer', 'algorithm'], default='parser',
                            help='choose which stage to start at, `path` arg is relative to stage (default=parser)')
        parser.add_argument('--final_stage', choices=['parser', 'featurizer', 'algorithm'],
                            default='algorithm', help='choose which stage to finish at (default=algorithm)')
        parser.add_argument('--groups', '-g', default='host',
                            help='groups of comma separated features to use (default=host)')
        parser.add_argument('--gzip', '-z', choices=['input', 'output', 'both'], default='both',
                            help='use gzip between stages, useful when not using all 3 stages (default=both)')
        parser.add_argument('--level', '-l', choices=['packet', 'flow', 'host'],
                            default='packet', help='level to make the output records (default=packet)')
        parser.add_argument('--operation', '-O', choices=['train', 'predict', 'eval'], default='predict',
                            help='choose which operation task to perform, train or predict (default=predict)')
        parser.add_argument('--output', '-o', default=None,
                            help='directory to write out any results files to')
        parser.add_argument('--rabbit', '-r', default=False, action='store_true',
                            help='Send prediction message to RabbitMQ')
        parser.add_argument('--threads', '-t', default=1, type=int,
                            help='number of async threads to use (default=1)')
        parser.add_argument('--verbose', '-v', choices=[
                            'DEBUG', 'INFO', 'WARNING', 'ERROR'], default='INFO', help='logging level (default=INFO)')
        parser.add_argument('--trained_model',
                            help='specify a path to load or save trained model')
        parser.add_argument('--label_encoder',
                            help='specify a path to load or save label encoder')
        parser.add_argument('--scaler',
                            help='specify a path to load or save scaler')
        parser.add_argument('--kfolds',
                            help='specify number of folds for k-fold cross validation')
        parser.add_argument('--eval_data',
                            help='path to eval CSV file, if training')
        parser.add_argument('--train_unknown',
                            help='Train on unknown roles')
        parsed_args = parser.parse_args(raw_args)
        return parsed_args

    def run_parser_stage(self, in_path):
        instance = PCAPToCSV(raw_args=[
            in_path, '-e', self.engine, '-l', self.level,
            '-o', self.output, '-t', str(self.threads), '-v', self.log_level])
        return instance.main()

    def run_featurizer_stage(self, in_path):
        instance = CSVToFeatures(raw_args=[
            in_path, '-c', '-g', self.groups, '-z', self.gzip_opt,
            '-o', self.output, '-t', str(self.threads), '-v', self.log_level])
        return instance.main()

    def run_algorithm_stage(self, in_path):
        raw_args = [in_path, '-O', self.operation, '-v', self.log_level]
        opt_args = ['trained_model', 'label_encoder', 'kfolds', 'scaler', 'eval_data', 'train_unknown']
        for opt_arg in opt_args:
            val = getattr(self, opt_arg, None)
            if val is not None:
                raw_args.extend(['--' + opt_arg, str(val)])
        instance = HostFootprint(raw_args=raw_args)
        return instance.main()

    def run_stages(self):
        stages = ('parser', 'featurizer', 'algorithm')
        stage_runners = {
            'parser': self.run_parser_stage,
            'featurizer': self.run_featurizer_stage,
            'algorithm': self.run_algorithm_stage}

        try:
            first_stage_index = stages.index(self.first_stage)
            final_stage_index = stages.index(self.final_stage)
        except ValueError:
            self.logger.error('Unknown first/final stage name')
            return

        if first_stage_index > final_stage_index:
            self.logger.error('Invalid first and final stage combination')
            return

        run_schedule = stages[first_stage_index:(final_stage_index+1)]
        result = self.in_path
        self.logger.info(f'running stages: {run_schedule}')

        run_complete = False
        try:
            for stage in run_schedule:
                runner = stage_runners[stage]
                result = runner(result)
            run_complete = True
        except Exception as err:
            self.logger.error(f'Could not run stage: {err}')

        uid = os.getenv('id', 'None')
        file_path = os.getenv('file_path', self.in_path)
        results_outputter = ResultsOutput(
            self.logger, __version__, self.rabbit)

        if run_complete:
            if self.final_stage == 'algorithm' and self.operation == 'predict':
                if self.output:
                    if os.path.isdir(self.output):
                        result_json_file = os.path.join(self.output, 'predict.json')
                    else:
                        result_json_file = self.output
                    with open(result_json_file, 'w') as result_json:
                        result_json.write(result)
                results_outputter.output_from_result_json(uid, file_path, result)
            else:
                results_outputter.output_invalid(uid, file_path, file_path)
        else:
            results_outputter.output_invalid(uid, file_path, file_path)

    def main(self, raw_args=None):
        parsed_args = NetworkML.parse_args(raw_args=raw_args)
        self.in_path = parsed_args.path
        self.algorithm = parsed_args.algorithm
        self.engine = parsed_args.engine
        self.first_stage = parsed_args.first_stage
        self.final_stage = parsed_args.final_stage
        self.groups = parsed_args.groups
        self.gzip_opt = parsed_args.gzip
        self.level = parsed_args.level
        self.operation = parsed_args.operation
        self.output = parsed_args.output
        self.rabbit = parsed_args.rabbit
        self.threads = parsed_args.threads
        self.log_level = parsed_args.verbose
        self.trained_model = parsed_args.trained_model
        self.label_encoder = parsed_args.label_encoder
        self.scaler = parsed_args.scaler
        self.kfolds = parsed_args.kfolds
        self.eval_data = parsed_args.eval_data

        log_levels = {'INFO': logging.INFO, 'DEBUG': logging.DEBUG,
                      'WARNING': logging.WARNING, 'ERROR': logging.ERROR}
        logging.basicConfig(level=log_levels[self.log_level])

        self.run_stages()


if __name__ == '__main__':
    start = time.time()
    NetworkML()
    end = time.time()
    elapsed = end - start
    human_elapsed = humanize.naturaldelta(datetime.timedelta(seconds=elapsed))
    logging.info(f'Elapsed Time: {elapsed} seconds ({human_elapsed})')
