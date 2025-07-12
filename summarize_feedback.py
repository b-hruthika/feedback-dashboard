import pandas as pd
from transformers import pipeline

# Load your data
df = pd.read_csv("multilabel_with_urgency.csv")

# Load summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Group feedback by categories and summarize
categories = ["Bug", "Complaint", "Feature Request", "Compliment", "General Feedback"]

for cat in categories:
    subset = df[df[cat] == 1]["feedback_text"].tolist()
    text = " ".join(subset[:10])  # summarizing top 10 for performance
    if text.strip():
        print(f"\n📌 Summary for {cat}:")
        print(summarizer(text, max_length=60, min_length=25, do_sample=False)[0]["summary_text"])
