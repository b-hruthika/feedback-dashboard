import pandas as pd

# Load your classified results
df = pd.read_csv("classified_feedback.csv")

# Clean the text: remove extra spaces and make everything lowercase
df["manual_category"] = df["manual_category"].str.strip().str.lower()
df["predicted_category"] = df["predicted_category"].str.strip().str.lower()

# Compare and calculate how many were correct
correct_matches = (df["manual_category"] == df["predicted_category"]).sum()
total_feedback = len(df)
accuracy = (correct_matches / total_feedback) * 100

print(f"\n✅ Total feedback entries: {total_feedback}")
print(f"✅ Correctly classified: {correct_matches}")
print(f"🎯 Accuracy: {accuracy:.2f}%")

# Optional: show mismatched rows to see what went wrong
print("\n⚠️ Mismatches:")
print(df[df["manual_category"] != df["predicted_category"]][["feedback_text", "manual_category", "predicted_category"]])
