import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/churn_model.pkl")


def predict_churn(customer_data):
    """
    Accept customer data and return prediction + probability
    """

    # Convert input into dataframe
    df = pd.DataFrame([customer_data])

    # Prediction
    prediction = model.predict(df)[0]

    # Probability
    probability = model.predict_proba(df)[0][1]

    return prediction, probability