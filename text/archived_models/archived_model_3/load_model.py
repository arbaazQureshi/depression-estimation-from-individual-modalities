import numpy as np

from keras.models import Model, Sequential, load_model
from keras.layers import Dense, CuDNNLSTM, Input, Concatenate, Dropout, Bidirectional
import keras

def load_model(location=None):

	if(location != None):
		model = keras.models.load_model(location)
		print("Loaded the model.")
		return model

	X = Input(shape = (400, 512,))
	X_gender = Input(shape = (1,))

	Y = Bidirectional(CuDNNLSTM(200, name = 'lstm_cell'))(X)
	Y = Dropout(rate = 0.3)(Y)

	Y = Concatenate(axis = -1)([Y, X_gender])

	Y = Dense(60, activation = 'relu')(Y)
	Y = Dropout(rate = 0.3)(Y)
	
	Y = Dense(1, activation = None)(Y)

	model = Model(inputs = [X, X_gender], outputs = Y)

	print("Created a new model.")

	return model