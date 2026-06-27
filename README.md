# 🚀 Insurance Risk and Cost Predictor API

A backend project built using **FastAPI** that integrates a pre-trained Machine Learning model to predict insurance cost and risk category through REST APIs.

## 📌 Project Overview

This project demonstrates how to deploy and serve a Machine Learning model using FastAPI. The application accepts user information through API requests, sends it to the trained model, and returns the predicted insurance cost and risk category through REST API.

## ✨ Features

- REST API using FastAPI
- Request validation using Pydantic
- ML model integration (`model.pkl`)
- Predict Insurance Cost
- Predict Risk Category
- JSON API responses
- Error handling using HTTP exceptions

## 🛠️ Tech Stack

- Python
- FastAPI
- Pydantic
- Scikit-learn (Pre-trained Model)
- Joblib
- Uvicorn

## 📂 Project Structure

Insurance-Risk-and-Cost-Predictor/
│
├── Model/
├── __pycache__/
├── config/
├── schema/
├── README.md
├── Train_Model.py
├── app.py
├── frontend.py
├── insurance.csv
└── requirements.txt


## 📥 Input

The API accepts user details such as:

- Age
- Gender
- Height
- Weight
- Annual Income
- Occupation
- City
- Smoking Status

## 📤 Output

The API returns:

- Estimated Insurance Cost
- Risk Category (Low / Medium / High)

## ▶️ Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

## 🎯 What I Learned

- Building REST APIs with FastAPI
- Request and response validation using Pydantic
- Loading a trained ML model
- Integrating ML predictions with FastAPI
- Returning structured JSON responses
- API testing with Swagger UI
