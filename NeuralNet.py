from keras.models import Sequential
from keras.layers import Dense
import keras.losses
import tensorflow as tf
from keras.layers import Dropout
import Setup
import numpy as np
import pandas as pd

class NN():
    def __init__(self, data):
        M1 = Setup.Init(data)
        self.fTrain, self.fTest, self.tTrain, self.tTest = M1.Features()
        self.fTrain = np.asarray(self.fTrain).astype('float32')
        print("here")
        print(self.fTrain)
        self.fTest = np.asarray(self.fTest).astype('float32')
        self.tTrain = np.asarray(self.tTrain).astype('float32')
        self.tTest = np.asarray(self.tTest).astype('float32')

    def M1(self):
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Dense(5, activation='relu', input_dim=5))
        model.add(tf.keras.layers.Dense(5, activation='relu'))
        model.add(tf.keras.layers.Dense(2, activation='relu'))
        model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
        optimizer = tf.keras.optimizers.RMSprop(lr=0.01)
        model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=[tf.keras.metrics.BinaryCrossentropy()])

        #verbose=0 sets output quiet
        history = model.fit(self.fTrain, self.tTrain, epochs = 10, verbose = 0)
        model.summary()
        history.history
        scores = model.evaluate(self.fTrain, self.tTrain)
        print("scores")
        print(scores)
        return
