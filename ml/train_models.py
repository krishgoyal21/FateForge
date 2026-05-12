import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_squared_error
import joblib
import os

# Load dataset
data = pd.read_csv("data/life_behavior_dataset.csv")

# -------------------------
# Define Features
# -------------------------

features = [
    "study_hours",
    "sleep_hours",
    "screen_time_hours",
    "workout_done",
    "mood_score",
    "deep_work_sessions",
    "streak_days",
    "goal_difficulty",
    "task_completion_rate",
    "stress_level",
    "breaks_taken",
    "weekend_recovery_score"
]

X = data[features]

# -------------------------
# CONSISTENCY MODEL
# -------------------------

y_consistency = data["consistency_label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y_consistency, test_size=0.2, random_state=42
)

consistency_model = RandomForestClassifier(n_estimators=100)

consistency_model.fit(X_train, y_train)

preds = consistency_model.predict(X_test)

consistency_acc = accuracy_score(y_test, preds)

print("Consistency Model Accuracy:", consistency_acc)

# -------------------------
# BURNOUT MODEL
# -------------------------

y_burnout = data["burnout_label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y_burnout, test_size=0.2, random_state=42
)

burnout_model = RandomForestClassifier(n_estimators=100)

burnout_model.fit(X_train, y_train)

preds = burnout_model.predict(X_test)

burnout_acc = accuracy_score(y_test, preds)

print("Burnout Model Accuracy:", burnout_acc)

# -------------------------
# GROWTH MODEL
# -------------------------

y_growth = data["growth_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y_growth, test_size=0.2, random_state=42
)

growth_model = RandomForestRegressor(n_estimators=100)

growth_model.fit(X_train, y_train)

preds = growth_model.predict(X_test)

mse = mean_squared_error(y_test, preds)

print("Growth Model MSE:", mse)

# -------------------------
# Save models
# -------------------------

os.makedirs("models", exist_ok=True)

joblib.dump(consistency_model, "models/consistency_model.pkl")
joblib.dump(burnout_model, "models/burnout_model.pkl")
joblib.dump(growth_model, "models/growth_model.pkl")

print("Models saved successfully.")