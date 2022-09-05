# !/usr/bin/env python3
#!/usr/bin/env python

import traceback
import sys

from preprocess import Preprocess

preprocess = Preprocess()

coins = {'btcusd': ['BTC/USD', './unprocessed_data/btcusd.csv', './btc-weights/btc-weights.h5'], 'ethusd': ['ETH/USD', './unprocessed_data/ethusd.csv', './eth-weights/eth-weights.h5']}

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
        dataframe = preprocess.load_dataframe(coinValues)
        dataset = dataframe['close']
        dataset = dataset.astype('float32')
        train, valid, test = preprocess.split_dataset(dataset=dataset)
        (trainX, trainY), (validX, validY), (testX, testY) = preprocess.reshape_dataset(train=train, valid=valid, test=test, look_back=72)
        model = preprocess.create_model(coin)
        model = preprocess.fit_model(model=model, trainX=trainX, trainY=trainY, validX=validX, validY=validY)
        model.save_weights(coin[2])
    except:
        print(traceback.format_exc())

if __name__ == "__main__":
    sys.exit(main())