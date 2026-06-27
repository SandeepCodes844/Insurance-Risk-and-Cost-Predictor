import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Insurance Cost Predictor",
    page_icon="💰",
)

st.title("💰 Insurance Cost Predictor")

st.write("Enter your details below and get an estimated insurance cost.")

# Input Fields

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

weight = st.number_input(
    "Weight (kg)",
    min_value=30.0,
    max_value=200.0,
    value=70.0
)

height = st.number_input(
    "Height (cm)",
    min_value=100.0,
    max_value=250.0,
    value=170.0
)

income_lpa = st.number_input(
    "Annual Income (LPA)",
    min_value=0.0,
    value=10.0
)

smoker = st.selectbox(
    "Smoker",
    ["yes", "no"]
)

city = st.text_input(
    "City",
    value="Delhi"
)

occupation = st.selectbox(
    "Occupation",
    [
        "student",
        "private job",
        "government job",
        "business owner",
        "self employed",
        "retired",
        "unemployed",
        "others"
    ]
)

# Predict Button

if st.button("Predict Insurance Cost"):

    payload = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:

            result = response.json()

            predicted_cost = result["predicted_insurance_cost"]
            category = result["category"]
            

            st.success(
                f"Estimated Insurance Cost: ₹ {predicted_cost:,.2f}"
            )

            st.info(f"Risk Category: {category}")

        else:
            st.error(
                f"API Error: {response.status_code}"
            )
            st.write(response.text)

    except Exception as e:
        st.error(f"Connection Error: {e}") 