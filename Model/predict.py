#import the ml model

import pandas as pd
import joblib


model = joblib.load("Model/model.pkl")

#MLFlow
MODEL_VERSION = '1.0.0'

def predict_output( user_input: dict):

    input_df = pd.DataFrame([user_input])

    output = model.predict(input_df)[0]
    return output
