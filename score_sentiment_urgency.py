import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# Load last step’s output
df = pd.read_csv("multilabel_feedback.csv")

def get_sentiment(text):
    vs = analyzer.polarity_scores(text)["compound"]
    if vs >= 0.05:
        return "Positive"
    elif vs <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def get_urgency(row):
    # Simple heuristic:
    if row["Negative"] == 1 or "bug" in row["feedback_text"].lower():
        return 5
    if "please" in row["feedback_text"].lower():
        return 3
    return 1

df["sentiment"] = df["feedback_text"].apply(get_sentiment)
df["urgency"]   = df.apply(get_urgency, axis=1)

df.to_csv("scored_feedback.csv", index=False)
print("✅ Sentiment & urgency attached -> scored_feedback.csv")
