from unicodedata import category

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
from Model.predict  import predict_output , MODEL_VERSION
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse



app = FastAPI()

# human readable
@app.get("/")
def home():
  return {'message': 'Insurance Premium Prediction API'}

# machine readable
@app.get("/health")
def health_check():
  return {
    'status': 'ok', 
    'model_version': MODEL_VERSION ,
    'model_status': 'ready'
    }
  


@app.post("/predict", response_model=PredictionResponse)
def predict_insurance_cost(data: UserInput):

    input_data = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_score': data.lifestyle_score,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    predicted_cost = predict_output(input_data)

    if predicted_cost < 10000:
        category = "Low risk"
    elif predicted_cost < 22000:
        category = "Medium risk"
    else:
        category = "High risk"

    return PredictionResponse(
        predicted_insurance_cost=round(predicted_cost, 2),
        category=category
    )