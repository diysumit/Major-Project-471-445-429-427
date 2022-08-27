#!/usr/bin/env python3

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.dataframe.io import read_json, read_csv

import argparse
import requests
import sys
import pandas as pd

from datetime import date, timedelta

parser = argparse.ArgumentParser(description="")

parser.add_argument('--runner', required=True, help='Specify Apache Beam Runner')
parser.add_argument('--input_path', required=True, help='Path to CSV file')
parser.add_argument('--output_path', required=True, help='Path to save results')

arguments = parser.parse_args()

#* arguments
input_path = arguments.input_path
output_path = arguments.output_path
runner = arguments.runner

#* coin list
coins = {'btcusd': ['BTC/USD', './unprocessed_data/btcusd.csv'],
         'ethusd': ['ETH/USD', './unprocessed_data/ethusd.csv']}

#* create beam pipeline options
#//// TODO: Implementation Required
def create_options() -> PipelineOptions:
      """
      def create_options() -> PipelineOptions:

            return beam pipeline options object
      """
      options = PipelineOptions(['--runner', runner])
      return options

#* get response from api and return json_obj
#//// TODO: Implementation Required
def get_data(coin: list) -> list:
    """
        def get_data(coin: list) -> None

            returns json_obj
    """
    key = '0ADD391A-E5EB-4991-9E08-ECEAA0A2958A'
    headers = {'X-CoinAPI-Key' : key}
    date_today = date.today()
    start_date = date_today - timedelta(days=365) # 7 years of data
    url = f"https://rest.coinapi.io/v1/exchangerate/{coin[0]}/history?period_id=1HRS&time_start={start_date}T00:00:00&time_end={date_today}T00:00:00&limit=100000"
    response = requests.get(url=url, headers=headers)
    return response.text

#* Writes PTransform to csv
def write_to_csv(data: beam.PTransform):
      pass

#* Saves json objects locally in csv_files
# TODO: Implementation Required
def save_data(data):
      with beam.Pipeline() as P:
            (
            P
            | read_json(data)
            | beam.Map(write_to_csv())
            )

# TODO: Implementation Required
def save_results():
      pass

# TODO: Implement Pipeline logic
def run(OPTIONS: PipelineOptions, input_path: str):
      with beam.Pipeline(options=OPTIONS) as P:
      (
      P 
      | read_csv(input_path)
      | beam.Map(save_results())
      )

def main():
      unprocessed_data = []
      for coin in coins:
            unprocessed_data.append(get_data(coin))
      OPTIONS = create_options()
      for json_obj in unprocessed_data:
            save_data(data=json_obj)
      run(OPTIONS=OPTIONS, input_path=input_path)

if __name__ == "__main__":
      sys.exit(main())