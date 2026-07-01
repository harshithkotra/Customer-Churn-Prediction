from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# ---------------------------------------
# Create FastAPI App
# ---------------------------------------

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predict whether a bank customer will churn",
    version="1.0"
)

# ---------------------------------------
# Load Trained Model
# ---------------------------------------

model = joblib.load("model/churn_pipeline.pkl")

# ---------------------------------------
# Input Schema
# ---------------------------------------

class Customer(BaseModel):
    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float

# ---------------------------------------
# Routes
# ---------------------------------------

@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is Running"
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }


@app.post("/predict")
def predict(customer: Customer):

    try:

        # Convert request to DataFrame
        input_df = pd.DataFrame([customer.model_dump()])

        # Predict class
        prediction = int(model.predict(input_df)[0])

        # Predict probability
        probability = float(model.predict_proba(input_df)[0][1])

        # Risk level
        if probability < 0.30:
            risk = "Low"
        elif probability < 0.70:
            risk = "Medium"
        else:
            risk = "High"

        return {
            "prediction": prediction,
            "churn_probability": round(probability, 4),
            "risk_level": risk
        }

    except Exception as e:

        return {
            "error": str(e)
        }