import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


# Load Dataset
df = pd.read_csv("insurance.csv")


# ---------------------------
# Feature Engineering
# ---------------------------

# BMI
df["bmi"] = df["weight"] / ((df["height"] / 100) ** 2)


# Lifestyle Score
def get_lifestyle_score(row):
    if row["smoker"] == "yes" and row["bmi"] > 30:
        return "high risk"
    elif row["smoker"] == "yes" or row["bmi"] > 30:
        return "medium risk"
    else:
        return "low risk"


df["lifestyle_score"] = df.apply(get_lifestyle_score, axis=1)


# Age Group
def get_age_group(age):
    if age < 30:
        return "young"
    elif age < 60:
        return "middle-aged"
    else:
        return "senior"


df["age_group"] = df["age"].apply(get_age_group)


# City Tier
def get_city_tier(city):
    if city in ["Mumbai", "Delhi", "Bangalore"]:
        return "tier 1"
    elif city in ["Pune", "Hyderabad", "Chennai"]:
        return "tier 2"
    else:
        return "tier 3"


df["city_tier"] = df["city"].apply(get_city_tier)


# ---------------------------
# Final Features
# ---------------------------

X = df[
    [
        "bmi",
        "lifestyle_score",
        "age_group",
        "city_tier",
        "income_lpa",
        "occupation",
    ]
]

y = df["insurance_cost"]


# Categorical Columns
categorical_features = [
    "lifestyle_score",
    "age_group",
    "city_tier",
    "occupation",
]


# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features,
        )
    ],
    remainder="passthrough",
)


# Pipeline
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "regressor",
            RandomForestRegressor(
                n_estimators=100,
                random_state=42,
            ),
        ),
    ]
)


# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)


# Train
model.fit(X_train, y_train)


# Evaluate
y_pred = model.predict(X_test)

score = r2_score(y_test, y_pred)

print(f"R2 Score: {score:.4f}")


# Save Model
joblib.dump(model, "model.pkl")

print("Model saved successfully!")