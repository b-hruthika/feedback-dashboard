import pandas as pd

# Load your existing synthetic feedback
df = pd.read_csv("synthetic_feedback.csv")

# Add an empty column for manual labeling
df["manual_category"] = ""

# Save it so you can label it manually in Excel or Google Sheets
df.to_csv("manual_labeled_feedback.csv", index=False)

print("✅ File 'manual_labeled_feedback.csv' created! Open it and fill the 'manual_category' column.")
