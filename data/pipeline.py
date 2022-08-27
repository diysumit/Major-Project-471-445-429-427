#!/usr/bin/env python3

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

import argparse
import requests
import sys

parser = argparse.ArgumentParser(description="")

parser.add_argument('--runner', required=True, help='Specify Apache Beam Runner')
parser.add_argument('--input_path', required=True, help='Path to CSV file')
parser.add_argument('--output_path', required=True, help='Path to save results')

arguments = parser.parse_args()

#* path of the csv file and path to save results
input_path = arguments.input_path
output_path = arguments.output_path
runner = arguments.runner

#* create beam pipeline options
# TODO: Implementation Required
def create_options():
      options = PipelineOptions('--runner', runner)
      return options

#* get data from api and save in csv file locally
# TODO: Implementation Required
def get_data():
    pass

# TODO: Implementation Required
def save_results():
      pass

# TODO: Implement Pipeline logic
def run(OPTIONS: PipelineOptions):
      P = beam.Pipeline(options=OPTIONS)
      (
      P 
      | beam.io.ReadFromText(input_path)
      | beam.Map(save_results(output_path))
      )

def main():
      get_data()
      OPTIONS = create_options()
      run(OPTIONS=OPTIONS)

if __name__ == "__main__":
      sys.exit(main())