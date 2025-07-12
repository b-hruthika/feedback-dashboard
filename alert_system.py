import pandas as pd
from datetime import datetime, timedelta

# Load data
df = pd.read_csv("scored_feedback.csv", parse_dates=["timestamp"], dayfirst=True, encoding="ISO-8859-1")



# Filter for last 7 days
last_week = df[df["timestamp"] >= (datetime.now() - timedelta(days=7))]

# 🔴 Check for negative sentiment spike
negative_count = last_week[last_week["sentiment"] == "negative"].shape[0]
total_count = last_week.shape[0]
neg_ratio = (negative_count / total_count) * 100 if total_count > 0 else 0

if neg_ratio > 40:
    print("🚨 Alert: High volume of negative feedback this week!")
    print(f"⚠️ {negative_count} out of {total_count} feedbacks are negative ({neg_ratio:.2f}%)")

# 🐞 Check for urgent bugs
urgent_bugs = last_week[(last_week["manual_category"] == "bug") & (last_week["urgency_score"] >= 0.7)]
if not urgent_bugs.empty:
    print("\n🐞 Urgent Bug Reports:")
    print(urgent_bugs[["timestamp", "feedback_text", "urgency_score"]])
else:
    print("\n✅ No urgent bugs reported this week.")
