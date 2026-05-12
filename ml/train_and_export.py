import os
import json
import random

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
EXPORT_DIR = os.path.join(BASE_DIR, "export")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(EXPORT_DIR, exist_ok=True)

def clamp(value, low, high):
    return max(low, min(high, value))

def make_sample():
    study_hours = round(random.uniform(0, 6), 1)
    sleep_hours = round(random.uniform(4, 9), 1)
    screen_time = round(random.uniform(1, 10), 1)
    workout = random.randint(0, 1)
    mood = random.randint(1, 10)
    deep_work = random.randint(0, 5)
    streak = random.randint(0, 30)

    consistency = (
        study_hours * 12
        + sleep_hours * 6
        - screen_time * 5
        + workout * 8
        + mood * 2
        + deep_work * 5
        + streak * 1.5
    )

    burnout = (
        study_hours * 8
        - sleep_hours * 7
        + screen_time * 4
        - workout * 5
        - mood * 2
        - deep_work * 1
    )

    growth = (
        study_hours * 10
        + deep_work * 7
        + streak * 2
        + workout * 4
        + mood * 2
        - screen_time * 3
    )

    return {
        "study_hours": study_hours,
        "sleep_hours": sleep_hours,
        "screen_time": screen_time,
        "workout": workout,
        "mood": mood,
        "deep_work": deep_work,
        "streak": streak,
        "consistency_score": round(clamp(consistency, 0, 100), 2),
        "burnout_score": round(clamp(burnout, 0, 100), 2),
        "growth_score": round(clamp(growth, 0, 100), 2),
    }

def export_rules():
    rules = {
        "consistency": {
            "study_hours": 12,
            "sleep_hours": 6,
            "screen_time": -5,
            "workout": 8,
            "mood": 2,
            "deep_work": 5,
            "streak": 1.5
        },
        "burnout": {
            "study_hours": 8,
            "sleep_hours": -7,
            "screen_time": 4,
            "workout": -5,
            "mood": -2,
            "deep_work": -1
        },
        "growth": {
            "study_hours": 10,
            "deep_work": 7,
            "streak": 2,
            "workout": 4,
            "mood": 2,
            "screen_time": -3
        }
    }

    with open(os.path.join(EXPORT_DIR, "model_rules.json"), "w") as f:
        json.dump(rules, f, indent=2)

def export_mock_dataset():
    rows = [make_sample() for _ in range(200)]

    with open(os.path.join(EXPORT_DIR, "sample_predictions.json"), "w") as f:
        json.dump(rows[:20], f, indent=2)

if __name__ == "__main__":
    export_rules()
    export_mock_dataset()
    print("Export complete. Files saved in ml/export/")