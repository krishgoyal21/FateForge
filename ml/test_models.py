import joblib
import pandas as pd

consistency_model = joblib.load("models/consistency_model.pkl")
burnout_model = joblib.load("models/burnout_model.pkl")
growth_model = joblib.load("models/growth_model.pkl")

sample = pd.DataFrame([{
    "study_hours": 3,
    "sleep_hours": 7,
    "screen_time_hours": 4,
    "workout_done": 1,
    "mood_score": 7,
    "deep_work_sessions": 2,
    "streak_days": 5,
    "goal_difficulty": 3,
    "task_completion_rate": 0.8,
    "stress_level": 4,
    "breaks_taken": 3,
    "weekend_recovery_score": 7
}])

consistency = consistency_model.predict(sample)[0]
burnout = burnout_model.predict(sample)[0]
growth = growth_model.predict(sample)[0]

print("Consistency:", consistency)
print("Burnout:", burnout)
print("Growth:", growth)