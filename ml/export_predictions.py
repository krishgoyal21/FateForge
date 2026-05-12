import joblib
import pandas as pd
import json
import os

consistency_model = joblib.load("models/consistency_model.pkl")
burnout_model = joblib.load("models/burnout_model.pkl")
growth_model = joblib.load("models/growth_model.pkl")

with open("input.json") as f:
    user_input = json.load(f)

sample = pd.DataFrame([user_input])

consistency = int(consistency_model.predict(sample)[0])
burnout = int(burnout_model.predict(sample)[0])
growth = float(growth_model.predict(sample)[0])

result = {
    "input": user_input,
    "consistency": consistency,
    "burnout": burnout,
    "growth": round(growth, 2)
}

os.makedirs("export", exist_ok=True)

with open("export/ml_predictions.json", "w") as f:
    json.dump(result, f, indent=2)

print("ML predictions exported successfully")
print(result) 