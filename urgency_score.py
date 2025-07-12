import pandas as pd
from transformers import pipeline

# Load your classified data
df = pd.read_csv("classified_with_sentiment.csv")

# Load zero-shot classifier model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define urgency labels
labels = ["urgent", "not urgent"]

# Score each feedback
def score_urgency(text):
    result = classifier(text, candidate_labels=labels)
    scores = dict(zip(result["labels"], result["scores"]))
    return scores.get("urgent", 0.0)

df["urgency_score"] = df["feedback_text"].apply(score_urgency)

# Save to new file
df.to_csv("urgency_scored_feedback.csv", index=False)
print("✅ Urgency scoring complete. Saved as 'urgency_scored_feedback.csv'")
