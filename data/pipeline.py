#!/usr/bin/env python3

import traceback
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.dataframe.io import read_json, read_csv
from apache_beam.dataframe.convert import to_dataframe, to_pcollection

import argparse
import requests
import sys
import json
import pandas as pd

pd.options.plotting.backend = 'plotly'

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
coins = {'btcusd': ['BTC/USD', 'btcusd.csv'],
         'ethusd': ['ETH/USD', 'ethusd.csv']}

#* create beam pipeline options
#//// TODO: Implementation Required
def create_options() -> PipelineOptions:
      """
      def create_options() -> PipelineOptions:

            return beam PipelineOptions object
      """
      options = PipelineOptions(['--runner', runner])
      return options

#* get response from api and return json_obj
#//// TODO: Implementation Required
def get_data(coin: list) -> requests.Response.text:
    """
        def get_data(coin: list) -> requests.Response.text

            returns json_obj
    """
    key = 'FAA10B2B-C744-43C1-90BC-D1D0A0007E4C'
# key = '3E0B48CC-DCD8-4A5C-B336-8DCD7F024521'
# key = '277A3033-99A9-47AE-AC2F-6C9E557F47B0'
# key = 'CD276776-814F-4E42-A603-1A97E774AB36'
# key = '133B3720-92C1-49FA-8B14-E6CFBB53EC7F'
#     key = '0ADD391A-E5EB-4991-9E08-ECEAA0A2958A'
    headers = {'X-CoinAPI-Key' : key}
    date_today = date.today()
    start_date = date_today - timedelta(days=365) #* 1 years of data

    #! FIX THIS: the api response it still skewed, need fixing
    url = f"https://rest.coinapi.io/v1/exchangerate/{coin[0]}/history?period_id=1HRS&time_start={start_date}T00:00:00&time_end={date_today}T00:00:00"
    response = requests.get(url=url, headers=headers)
    return response.text

#* Saves json objects locally in csv_files
#//// TODO: Implementation Required
def save_data(data, filename) -> None:
      data = pd.DataFrame.from_dict([json.loads(data)])
      data.to_csv(f"{input_path}{filename}")

# TODO: Implementation Required
def save_results(df: pd.DataFrame) -> None:
      print(df)
      plot = df.plot()
      fig = plot.get_figure()
      fig.savefig(f"{output_path}result.png")

# TODO: Implement Pipeline logic
def run(OPTIONS: PipelineOptions, filename: str) -> None:
      
      with beam.Pipeline(options=OPTIONS) as P:

            csv_file = P | "Read CSV files" >> read_csv(input_path+filename)
            df = to_dataframe(pcoll=csv_file)
            (df | "Save results" >> beam.Map(save_results()))               

def main() -> None:
      try:
            unprocessed_data = []
            for coin in coins:
                  unprocessed_data.append(get_data(coin))
            OPTIONS = create_options()
            for json_obj, coin in zip(unprocessed_data, coins):
                  filename = coins.get(coin)[1]
                  save_data(data=json_obj, filename=filename)
                  run(OPTIONS=OPTIONS, filename=filename)
     
      except Exception as e:
            traceback.print_exc(e)

if __name__ == "__main__":
      sys.exit(main())