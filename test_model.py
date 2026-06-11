import joblib

print("Step 1")

model = joblib.load("models/churn_model.pkl")

print("Step 2")

print(type(model))

print("Finished")