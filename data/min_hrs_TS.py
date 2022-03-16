#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

def minute_to_hour():
    df = pd.read_csv('./unprocessed_data/btcusd.csv', parse_dates=['time'])
    new_df = pd.DataFrame()
    new_df['time'] = df['time'].dt.date
    print(new_df['time'])
    return new_df

minute_to_hour()