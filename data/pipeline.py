#!/usr/bin/env python3

import apache_beam as beam
from apache_beam.options import pipeline_options

import argparse
import requests
import sys

parser = argparse.ArgumentParser(description="")

parser.add_argument()
parser.add_argument()

arguments = parser.parse_args()

#* path of the csv file
path = ''

#* create beam pipeline options
# TODO: Implementation Required
def create_options():
      pass

#* get data from api and save in csv file locally
# TODO: Implementation Required
def get_data():
    pass

def save_results():
      pass

# TODO: Implement Pipeline logic
def run(OPTIONS: pipeline_options):
      P = beam.Pipeline(options=OPTIONS)
      (
      P 
      | beam.io.ReadFromText(path)
      | beam.Map(save_results())
      )

def main():
      get_data()
      OPTIONS = create_options()
      run(OPTIONS=OPTIONS)

if __name__ == "__main__":
      sys.exit(main())