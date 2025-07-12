import pandas as pd
import matplotlib.pyplot as plt

# -------- PART 1: Sentiment Trend -------- #
df = pd.read_csv("scored_feedback.csv", parse_dates=["timestamp"])

weekly_sentiment = (
    df.set_index("timestamp")
      .groupby("sentiment")["feedback_text"]
      .resample("W").count()
      .unstack(0)
      .fillna(0)
)

weekly_sentiment.to_csv("trend_report_sentiment.csv")
print("✅ Weekly sentiment trend -> trend_report_sentiment.csv")

# -------- PART 2: Category Trend -------- #
# Load updated multilabel file with categories like Bug, Complaint, etc.
df_cat = pd.read_csv("multilabel_with_urgency.csv", parse_dates=["timestamp"])

# Choose only category columns
category_columns = ["Bug", "Complaint", "Feature Request", "Compliment", "General Feedback"]

weekly_category = (
    df_cat.set_index("timestamp")[category_columns]
          .resample("W").sum()
)

weekly_category.to_csv("trend_report_categories.csv")
print("✅ Weekly category trend -> trend_report_categories.csv")

# Optional: Save as chart
weekly_category.plot(figsize=(12, 6), title="Category Trends Over Time")
plt.xlabel("Week")
plt.ylabel("Feedback Count")
plt.grid(True)
plt.tight_layout()
plt.savefig("trend_analysis.png")
print("📊 Chart saved as 'trend_analysis.png'")
