#!/usr/bin/env python3

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.dataframe.io import read_json, read_csv
from apache_beam.dataframe.convert import to_dataframe, to_pcollection

import argparse
import requests
import sys
import modin.pandas as pd

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
def get_data(coin: list) -> requests.Response.text:
    """
        def get_data(coin: list) -> None

            returns json_obj
    """
    key = 'FAA10B2B-C744-43C1-90BC-D1D0A0007E4C'
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
def save_data(data, path):
      P = beam.Pipeline()
      df = (
            P
            | "Read Json Objects" >> read_json(data)
            | "Convert PTransform to DataFrame" >> to_dataframe() #! doesn't work api response is skewed
            )
      df.to_csv(path)

# TODO: Implementation Required
def save_results():
      pass

# TODO: Implement Pipeline logic
def run(OPTIONS: PipelineOptions, input_path: str):
      with beam.Pipeline(options=OPTIONS) as P:
            (
            P 
            | "Read CSV files" >> read_csv(input_path)
            | "Save results" >> beam.Map(save_results())
            )

def main():
      unprocessed_data = []
      for coin in coins:
            unprocessed_data.append(get_data(coin))
      OPTIONS = create_options()
      for json_obj, coin in zip(unprocessed_data, coins):
            save_data(data=json_obj, path=coin[1])
      run(OPTIONS=OPTIONS, input_path=input_path)

if __name__ == "__main__":
      sys.exit(main())