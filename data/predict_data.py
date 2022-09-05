#!/usr/bin/env python3

import pandas as pd
import numpy
import matplotlib.pyplot as plt
import tensorflow as tf

numpy.random.seed(10)

dataframe = pd.read_csv('./processed_data/btcusdcomplete.csv', parse_dates=['time_close'])
dataframe['time_close'] = pd.to_datetime(dataframe['time_close'], unit='s')
dataframe = dataframe.set_index('time_close')

#* convert an array of values into a dataset matrix
def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		a = dataset[i:(i+look_back)]
		dataX.append(a)
		dataY.append(dataset[i + look_back])
	return (numpy.array(dataX), numpy.array(dataY))


#* load the dataset
dataset = dataframe['rate_close']
dataset = dataset.astype('float32')
#* dataset = dataset[-4380:]

#* split into training, validation and testing sets in 70, 20 and 10 percents respectively
train_size = int(len(dataset)*0.70)
valid_size = int(len(dataset)*0.20)
train = dataset[:train_size]
valid = dataset[train_size:train_size+valid_size]
test = dataset[train_size+valid_size:]

#* reshape datasets
look_back = 72
trainX, trainY = create_dataset(train, look_back=look_back)
validX, validY = create_dataset(valid, look_back=look_back)
testX, testY = create_dataset(test, look_back=look_back)

# *creating callbacks to save model
# cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath='./eth-model/',
#                                                  save_weights_only=True,
#                                                  verbose=1)
print(f'{trainX.shape} {trainY.shape}')
#* model creation and fitting
model = tf.keras.Sequential([
	tf.keras.layers.LSTM(24, input_shape=(look_back, 1),
	                     activation=tf.nn.relu, return_sequences=True),
	tf.keras.layers.Bidirectional(
		tf.keras.layers.LSTM(12, activation=tf.nn.relu)),
	tf.keras.layers.Flatten(),
	tf.keras.layers.Dense(1),
])

model.compile(loss=tf.keras.losses.MeanSquaredError(),
              optimizer=tf.keras.optimizers.Adam())

model.fit(trainX, trainY, epochs=15, batch_size=5,
          verbose=2, validation_data=(validX, validY))

# model.save_weights('./btc-weights/')

#* generate predictions for training
trainPredict = model.predict(trainX)
validPredict = model.predict(validX)
testPredict = model.predict(testX)

#* shift train predictions for plotting
trainPredictPlot = numpy.empty_like(dataset)
trainPredictPlot[:] = numpy.nan
trainPredictPlot[look_back:len(
	trainPredict)+look_back] = numpy.squeeze(trainPredict)

#* shift valid predictions for plotting
validPredictPlot = numpy.empty_like(dataset)
validPredictPlot[:] = numpy.nan
validPredictPlot[len(trainPredict)+look_back:len(trainPredict) +
                 valid_size-1] = numpy.squeeze(validPredict)

#* shift test predictions for plotting
testPredictPlot = numpy.empty_like(dataset)
testPredictPlot[:] = numpy.nan
testPredictPlot[len(trainPredict)+valid_size+(look_back*2) +
                1:len(dataset)-1] = numpy.squeeze(testPredict)

plt.plot(dataframe.index.values, dataframe['rate_close'], 'r-', label='Real')
plt.plot(dataframe.index.values, trainPredictPlot,
         color='green', label='Training Predictions')
plt.plot(dataframe.index.values, validPredictPlot,
         color='blue', label='Validation Predictions')
plt.plot(dataframe.index.values, testPredictPlot,
         color='orange', label='Testing Predictions')
plt.xlabel('Date')
plt.ylabel('Values')
plt.title('Results')
plt.legend()
plt.show()