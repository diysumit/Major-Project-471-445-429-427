#!/usr/bin/env python3

"""

Download or Update data

"""

import os
import sys
import traceback

from datetime import date, timedelta
from preprocess import Preprocess

preprocess = Preprocess()

date_today = date.today()
start_date = date_today - timedelta(days=180)

filepath = './unprocessed_data/'

coins = {'btcusd': ['BTC/USD', './unprocessed_data/btcusd.csv'], 'ethusd': ['ETH/USD', './unprocessed_data/ethusd.csv']}

key = 'FAA10B2B-C744-43C1-90BC-D1D0A0007E4C'
# key = '3E0B48CC-DCD8-4A5C-B336-8DCD7F024521'
# key = '277A3033-99A9-47AE-AC2F-6C9E557F47B0'
# key = 'CD276776-814F-4E42-A603-1A97E774AB36'
# key = '133B3720-92C1-49FA-8B14-E6CFBB53EC7F'

headers = {'X-CoinAPI-Key' : key}


def download_csv(coin: list, start: date, end: date) -> None:
    """
        def download_csv(coin: list, start: date, end: date) -> None

            writes coin.csv files in uprocessed_data folder
    """
    url = f"https://rest.coinapi.io/v1/exchangerate/{coin[0]}/history?period_id=1HRS&time_start={start}T00:00:00&time_end={end}T00:00:00&limit=100000"
    lists = preprocess.get_lists(url, headers)
    time_step, rate_close = preprocess.list_from_dict(lists)
    print(f"Writing {coin[0]}.csv file")
    preprocess.write_csv(filepath=coin[1], time_steps=time_step, rate_close=rate_close)
    
def update_csv(coin: list, start: date, end: date) -> None:
    """
        def update_csv(coin: list) -> None

            updates coin.csv with new data in uprocessed_data folder
    """
    url = f"https://rest.coinapi.io/v1/exchangerate/{coin[0]}/history?period_id=1HRS&time_start={start}T00:00:00&time_end={end}T00:00:00&limit=100000"
    lists = preprocess.get_lists(url, headers)
    time_steps, rate_close = preprocess.list_from_dict(lists)
    preprocess.write_csv(filepath=coin[1], time_steps=time_steps, rate_close=rate_close)

def main() -> None:
    """
        Driver Function
    """
    try:
        if not os.path.exists(filepath):
            print(f'Creating folder {filepath}')
            os.mkdir(filepath)
        
        for coin in coins.values():
            if os.path.exists(coin[1]):
                last_date = preprocess.get_last_date(coin[1])
                update_csv(coin=coin, start=date_today, end=last_date)
            else:
                download_csv(coin=coin, start=date_today, end=start_date)

    except Exception:
        print(traceback.format_exc())

if __name__ == "__main__":
    sys.exit(main())