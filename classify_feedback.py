import pandas as pd
from transformers import pipeline

# Load the feedback data
df = pd.read_csv("final_feedback_data.csv")

# Create a zero-shot classifier using a Hugging Face model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define the feedback categories
labels = ["Bug", "Complaint", "Compliment", "Feature Request", "General Feedback"]

# Classify each feedback row
def classify(text):
    result = classifier(text, labels)
    return result['labels'][0]  # Pick the top predicted label

df["predicted_category"] = df["feedback_text"].apply(classify)

# Save the output to a new file
df.to_csv("classified_feedback.csv", index=False)

print("✅ Done! Results saved to 'classified_feedback.csv'")
