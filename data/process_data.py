#!/usr/bin/env python3

import pandas as pd
import sys
import os

from min_hrs_TS import minute_to_hour
from datetime import datetime
from glob import glob
from multiprocessing import Pool

# command line argumnet to force update the file even when they are present in processed folder
# -u or -U or or update
update = ""
try:
    update = sys.argv[1]
except IndexError as e:
    update = ""


if not os.path.exists('./unprocessed_data/') and len(os.listdir('./unprocessed_data/')) < 2:
    print("""
    Necessary CSV files not found.\n
    Run setup.sh
    and then run process_data.py\n
    """)
    sys.exit(1)

if not os.path.exists('./processed_data/'):
    print('Making new folder in current directory to save processed datasets: processed_data')
    os.mkdir('./processed_data/')

file_location = os.path.abspath('.') + '/unprocessed_data/'
unprocessed_files = glob(file_location + '*.csv')
save_location = os.path.abspath('.') + '/processed_data/'
processed_files = glob(save_location + '*.csv')

def timestamp_conversion(df):
    """Converts unix timestamps to utc date and returns dataframe\n
        def timestamp_conversion(df):\n
            df['time'] = (df['time']/1000.0).apply(datetime.fromtimestamp)\n            
            return df
    """
    df['time'] = (df['time']/1000.0).apply(datetime.fromtimestamp)
    return df

def main():
    try:
        print('Processing Files Now:')
        for file in unprocessed_files:
            if (os.path.basename(file) not in list(map(os.path.basename, processed_files))
                or update.lower() == "update"
                or update.lower() == "-u"):
                print(f'\t{os.path.basename(file)}')
                df = pd.read_csv(file)
                df = timestamp_conversion(df)
                df.to_csv(save_location+os.path.basename(file), index=False)
            else:
                print('\tSkipping File')
    except Exception as e:
        print(f'An exception ocurred: {e}')

if __name__ == "__main__":
    sys.exit(main())