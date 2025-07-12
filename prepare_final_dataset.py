import pandas as pd

# Load the manually labeled file
df = pd.read_csv("manual_labeled_feedback.csv")

# Keep only the required columns
df = df[['feedback_text', 'source', 'timestamp', 'manual_category']]

# Clean the data
df.drop_duplicates(inplace=True)
df.dropna(subset=['feedback_text'], inplace=True)

# Save to a final CSV
df.to_csv("final_feedback_data.csv", index=False)
print("✅ final_feedback_data.csv created successfully.")
