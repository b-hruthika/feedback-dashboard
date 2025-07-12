import pandas as pd

# Load the multilabel file
df = pd.read_csv("multilabel_feedback.csv")

# Define simple urgency rules based on keywords
def score_urgency(text):
    text = text.lower()
    if any(word in text for word in ["crash", "fail", "not working", "broken", "freeze", "stuck", "deducted", "blocked"]):
        return "High"
    elif any(word in text for word in ["slow", "bug", "delay", "lag", "issue", "verify", "reset", "problem"]):
        return "Medium"
    else:
        return "Low"

# Apply the function
df["urgency"] = df["feedback_text"].apply(score_urgency)

# Save
df.to_csv("multilabel_with_urgency.csv", index=False)
print("✅ Urgency scoring complete!")
