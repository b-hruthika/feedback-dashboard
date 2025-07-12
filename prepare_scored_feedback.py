import pandas as pd

# Load your latest CSVs
df_classified = pd.read_csv("classified_with_sentiment.csv")  # Sentiment already added here
df_urgency = pd.read_csv("urgency_scored_feedback.csv")       # Contains urgency_score
df_confidence = pd.read_csv("multilabel_feedback.csv")        # Contains confidence_score

# Merge all on common fields — assuming feedback_text is unique
df = df_classified.merge(df_urgency[["feedback_text", "urgency_score"]], on="feedback_text", how="left")
df = df.merge(df_confidence[["feedback_text", "confidence_score"]], on="feedback_text", how="left")

# Optional: Keep only needed columns
columns = [
    "feedback_text", "manual_category", "predicted_category",
    "sentiment", "urgency_score", "confidence_score", "timestamp"
]
df = df[columns]

# Save final dataset
df.to_csv("scored_feedback.csv", index=False)
print("✅ Final scored dataset saved as 'scored_feedback.csv'")
