import random
import csv

rows = []

for i in range(5000):

    study_hours = round(random.uniform(0,6),1)
    sleep_hours = round(random.uniform(4,9),1)
    screen_time = round(random.uniform(1,10),1)
    workout = random.randint(0,1)
    mood = random.randint(1,10)
    deep_work = random.randint(0,5)
    streak = random.randint(0,30)
    goal_difficulty = random.randint(1,5)
    completion = round(random.uniform(0.1,1),2)
    stress = random.randint(1,10)
    breaks = random.randint(0,5)
    recovery = random.randint(1,10)

    # consistency rule
    if sleep_hours > 6 and completion > 0.6 and stress < 7:
        consistency = 1
    else:
        consistency = 0

    # burnout rule
    if stress > 7 and sleep_hours < 6:
        burnout = 2
    elif stress > 5:
        burnout = 1
    else:
        burnout = 0

    # growth formula
    growth = int(
        study_hours*8 +
        deep_work*6 +
        streak*1.5 +
        completion*20 -
        screen_time*2
    )

    growth = max(0, min(100, growth))

    rows.append([
        study_hours,
        sleep_hours,
        screen_time,
        workout,
        mood,
        deep_work,
        streak,
        goal_difficulty,
        completion,
        stress,
        breaks,
        recovery,
        consistency,
        burnout,
        growth
    ])

with open("life_behavior_dataset.csv", "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
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
        "weekend_recovery_score",
        "consistency_label",
        "burnout_label",
        "growth_score"
    ])

    writer.writerows(rows)

print("Dataset generated successfully with 5000 rows!")