# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:31:54 2024

@author: alihasrat
"""
import requests
import json

url = 'http://127.0.0.1:8000/diabetes_prediction'

input_data_for_model = {
    
    'Pregnancies': 6,
    'Glucose': 148,
    'BloodPressure': 72,
    'SkinThickness': 35,
    'Insulin': 0,
    'BMI': 33.6,
    'DiabetesPedigreeFunction': 0.627,  # Corrected field name
    'Age': 50
}

input_json = json.dumps(input_data_for_model)
response = requests.post(url, json=input_data_for_model)  # Pass json parameter instead of data

print(response.text)
