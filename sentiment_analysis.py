import pandas as pd
from transformers import pipeline

# Load your classified feedback
df = pd.read_csv("classified_feedback.csv")

# Load Hugging Face sentiment analysis pipeline
sentiment_model = pipeline("sentiment-analysis")

# Apply sentiment analysis to each feedback
df["sentiment"] = df["feedback_text"].apply(lambda x: sentiment_model(x)[0]['label'])

# Save the updated data
df.to_csv("classified_with_sentiment.csv", index=False)

print("✅ Sentiment analysis complete! Results saved to 'classified_with_sentiment.csv'")
