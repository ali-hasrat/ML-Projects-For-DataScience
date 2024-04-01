# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('E:/Deploy ML/trained_model.sav', 'rb'))

input_data = (111,1000,7226,33,78,87.5,0.197,26)

# changing the input_data to a Numpy Array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)   # this will tell the model that we are not giving 768 examples but only one data point.

# standardize the input data
# std_data = scaler.transform(input_data_reshaped)
# print(std_data)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if prediction[0] == 0:
  print("The Person is not Diabetic.")

else:
  print("The Person is Diabetic")