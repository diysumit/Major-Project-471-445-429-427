import requests
import json
import csv
import matplotlib.pyplot as plt
import os

from datetime import datetime

class Preprocess:
    """Helper functions for preprocessing and saving and retrieving crypto-exchangerate data"""
    def __init__(self):
        pass

    def get_lists(self, url: str, headers: dict) -> list:
        """
            def get_lists(self, url: str, headers: dict) -> list

                returns list_of_dictionaries
        """
        response = requests.get(url=url, headers=headers)
        lists = json.loads(response.text)
        return lists

    def list_from_dict(self, lists: list) -> tuple:
        """
            def list_from_dict(self, lists: list) -> tuple

                returns (time_steps, rate_close)
        """
        time_steps = ['time']
        rate_close = ['close']
        for dictionary in lists:
            date_string = dictionary.get('time_close')[:-9]
            datetimeObj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
            time_steps.append(datetimeObj.timestamp())
            rate_close.append(dictionary.get('rate_close'))

        return (time_steps, rate_close)

    def write_csv(self, filepath: str, time_steps: list, rate_close: list) -> None:
        """
            def write_csv(self, filename: str, time_steps: list, rate_close: list) -> None

                writes time_steps and rate_low to a csv file
        """
        
        if len(time_steps) == 0 or len(rate_close) == 0 or not os.path.exits(filepath):
            time_steps.append('time')
            rate_close.append('close')

        with open(filepath, 'a+') as csvfile:
            writer = csv.writer(csvfile)
            for i in range(len(time_steps)):
                writer.writerow([time_steps[i], rate_close[i]])

    def read_csv(self, filepath: str) -> tuple:
        """
            def read_csv(self, filepath: str) -> tuple

                returns time_steps and rate_low lists
        """
        time_steps = []
        rate_close = []
        with open(filepath) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            for column in reader:
                time_steps.append(float(column[0]))
                rate_close.append(float(column[1]))
        return (time_steps, rate_close)

    def plot_series(time: list, series: list, format="-", start=0, end=None, name='fig.jpg', figsize=(10, 6)) -> None:
        """
            def plot_series(time: list, series: list, format="-", start=0, end=None, name='fig.jpg', figsize=(10, 6))

                plots figure for given parameters
        """
        plt.figure(figsize=figsize)
        plt.plot(time[start:end], series[start:end], format)
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.grid(True)
        plt.savefig(name)
        

    def get_last_date(self, filepath: str) -> datetime:
        """
            def get_last_date(coin: list

                returns last date when coin.csv file was updated
        """
        time_steps_coin, _ = self.read_csv(filepath)
        last_date_coin = datetime.fromtimestamp(time_steps_coin[-1])

        return last_date_coin
