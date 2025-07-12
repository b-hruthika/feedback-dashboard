import pandas as pd
import os

df = pd.read_csv("scored_feedback.csv", parse_dates=["timestamp"], encoding="ISO-8859-1")


os.makedirs("reports", exist_ok=True)

# Category-wise Weekly Summary
weekly_category = df.groupby(pd.Grouper(key="timestamp", freq="W"))["manual_category"].value_counts().unstack().fillna(0)
weekly_category.to_csv("reports/weekly_category_summary.csv")

# Sentiment Weekly Summary
weekly_sentiment = df.groupby(pd.Grouper(key="timestamp", freq="W"))["sentiment"].value_counts().unstack().fillna(0)
weekly_sentiment.to_csv("reports/weekly_sentiment_summary.csv")

# Urgency Weekly Average
weekly_urgency = df.groupby(pd.Grouper(key="timestamp", freq="W"))["urgency_score"].mean()
weekly_urgency.to_csv("reports/weekly_urgency_average.csv")

print("✅ All enhanced weekly summaries saved in 'reports/' folder.")
