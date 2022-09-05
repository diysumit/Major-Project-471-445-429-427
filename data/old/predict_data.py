#!/usr/bin/env python3

import sys
import traceback

import pandas as pd
from preprocess import Preprocess

preprocess = Preprocess()

coins = {'btcusd': ['BTC/USD', './unprocessed_data/btcusd.csv', './btc-weights/btc-weights.h5'], 'ethusd': ['ETH/USD', './unprocessed_data/ethusd.csv', './eth-weights/eth-weights.h5']}

# hyper-parameters
look_back = 72

# getting parameters from command line
coin = ""
try:
    if sys.argv[1]:
        coin = str(sys.argv[1])
except:
    coin = 'btcusd'

def main():
    try:
        coinValues = coins.get(coin)
        time_step, rate_close = preprocess.read_csv(coinValues[1])
        time = pd.Series(time_step[-look_back:])
        time = pd.to_datetime(time,unit='s')
        value = pd.Series(rate_close[-look_back:])
        model = preprocess.create_model(coinValues)
        train, valid, test = preprocess.split_dataset(dataset=value)
        (trainX, trainY), (validX, validY), (testX, testY) = preprocess.reshape_dataset(train=train, valid=valid, test=test, look_back=look_back)
        trainPredict, validPredict, testPredict = preprocess.generate_predictions(model=model, trainX=trainX, validX=validX, testX=testX)
        trainPredictPlot = preprocess.shift_prediction(dataset=value, predict=trainPredict, train=True, train_size=train)
        validPredictPlot = preprocess.shift_prediction(dataset=value, predict=validPredict, valid=True, train_size=train, valid_size=valid)
        testPredictPlot = preprocess.shift_prediction(dataset=value, predict=testPredict, test=True, train_size=train, valid_size=valid)
        preprocess.plot_series(dataframe=value, predictPlot=trainPredictPlot, color='green', label='Training Predictions')
        preprocess.plot_series(dataframe=value, predictPlot=validPredictPlot, color='blue', label='Validation Predictions')
        preprocess.plot_series(dataframe=value, predictPlot=testPredictPlot, color='orange', label='Testing Predictions')
    except:
        print(traceback.format_exc())
