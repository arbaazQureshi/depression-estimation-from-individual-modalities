import numpy as np
import pandas as pd




def load_training_data():

	batch_size = 21
	
	train_set_ID_list = [303, 304, 305, 310, 312, 313, 315, 316, 317, 318, 319, 320, 321, 322, 324, 325, 326, 327, 328, 330, 333, 336, 338, 339, 340, 341, 343, 344, 345, 347, 348, 350, 351, 352, 353, 355, 356, 357, 358, 360, 362, 363, 364, 366, 368, 369, 370, 371, 372, 374, 375, 376, 379, 380, 383, 385, 386, 391, 392, 393, 397, 400, 401, 409, 412, 414, 415, 416, 419, 423, 425, 426, 427, 428, 429, 430, 433, 434, 437, 441, 443, 445, 446, 447, 448, 449, 454, 455, 456, 457, 459, 463, 464, 468, 471, 473, 474, 475, 478, 479, 485, 486, 487, 488, 491]

	location = '/home/syedcs15/depression_estimation/preprocessed_data/training_data/transcript/preprocessed_semantic_vectors/training_vectors.npy'
	X = np.load(location)
	
	labels = pd.read_csv('/home/syedcs15/depression_estimation/labels/train_split_Depression_AVEC2017.csv')
	labels.set_index('Participant_ID', inplace = True)

	Y = labels['PHQ8_Score'][train_set_ID_list].values.tolist()
	X_gender = labels['Gender'][train_set_ID_list].values

	print("Training data is loaded.")

	return (X, Y, X_gender)





def load_development_data():

	dev_set_ID_list = [302, 307, 331, 335, 346, 367, 377, 381, 382, 388, 389, 390, 395, 403, 404, 406, 413, 417, 418, 420, 422, 436, 439, 440, 472, 476, 477, 482, 483, 484, 489, 490, 492]


	location = '/home/syedcs15/depression_estimation/preprocessed_data/development_data/transcript/preprocessed_semantic_vectors/dev_vectors.npy'
	X = np.load(location)

	labels = pd.read_csv('/home/syedcs15/depression_estimation/labels/dev_split_Depression_AVEC2017.csv')
	labels.set_index('Participant_ID', inplace = True)
	
	Y = labels['PHQ8_Score'][dev_set_ID_list].values.tolist()

	X_gender = labels['Gender'][dev_set_ID_list].values

	print("Development data is loaded")

	return (X, Y, X_gender)