import pandas as pd
from transformers import pipeline

# Step 1: Load classified feedback
df = pd.read_csv("classified_feedback.csv")

# Step 2: Load sentiment and summarization models
sentiment_pipeline = pipeline("sentiment-analysis")
summarization_pipeline = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Step 3: Apply sentiment and summarization
df["sentiment"] = df["feedback_text"].apply(lambda x: sentiment_pipeline(x)[0]["label"])
df["summary"] = df["feedback_text"].apply(lambda x: summarization_pipeline(x, max_length=30, min_length=5, do_sample=False)[0]["summary_text"])

# Step 4: Save result
df.to_csv("chained_feedback.csv", index=False)
print("✅ Prompt chaining complete! Results saved to 'chained_feedback.csv'")
