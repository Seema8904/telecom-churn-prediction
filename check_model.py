import joblib

model = joblib.load("models/churn_model.pkl")

print("Model Type:")
print(type(model))

if hasattr(model, "feature_names_in_"):
    print("\nFeatures expected by model:")
    print(model.feature_names_in_)
else:
    print("\nNo feature_names_in_ found")