import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from formatData import *

class neuralModel(object):
    def __init__(self):
        self.model=Sequential()
    def createModel(self):

        outcomes = 3
        self.model.add(Dense(200, activation='relu', input_shape=(30, )))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(125, activation='relu'))
        self.model.add(Dense(75, activation='relu'))
        self. model.add(Dropout(0.1))
        self. model.add(Dense(25, activation='relu'))
        self. model.add(Dense(outcomes, activation='softmax'))
        optimizer = tf.keras.optimizers.Adam(0.0001)
        self. model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['acc'])

    def trainModel(self,trainingData):
        tensorData=compileToNumpy(trainingData)
        X=tensorData[0]
        y=tensorData[1]


        import sklearn.model_selection as ms
        X_train, X_test, y_train, y_test = ms.train_test_split(X, y, test_size=0.1)


        #train neural network using tensor data
        self.model.fit(X_train,y_train,batch_size=256,epochs=10, validation_data=(X_test,y_test),shuffle=True,use_multiprocessing=True,workers=8,verbose=1)
