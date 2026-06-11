import joblib
import pandas as pd

model = joblib.load("models/churn_model.pkl")

def predict_churn(customer_data):

    df = pd.DataFrame([customer_data])
    print("INPUT FEATURES:")
    print(df.columns.tolist())
    print("MODEL FEATURES:")
    print(model.feature_names_in_.tolist())
    try:
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1]

        return prediction, probability

    except Exception as e:
        print("\nINPUT COLUMNS:")
        print(df.columns.tolist())

        print("\nMODEL COLUMNS:")
        print(model.feature_names_in_.tolist())

        print("\nERROR:")
        print(e)

        raise