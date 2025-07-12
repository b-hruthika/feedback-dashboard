import pandas as pd
from transformers import pipeline

# Load your feedback
df = pd.read_csv("classified_feedback.csv")
feedbacks = df["feedback_text"].tolist()

# Load a better instruction-following model
classifier = pipeline("text2text-generation", model="google/flan-t5-base")

# Define prompt templates
def zero_shot_prompt(text):
    return f"Classify the following feedback into one of these categories: Bug, Feature Request, Complaint, Compliment, General Feedback.\n\nFeedback: {text}\nCategory:"

def few_shot_prompt(text):
    return f"""Classify the feedback below.

Example 1:
Feedback: The app crashes every time I try to upload a photo.
Category: Bug

Example 2:
Feedback: Please add an offline mode.
Category: Feature Request

Now classify this:
Feedback: {text}
Category:"""

def chain_of_thought_prompt(text):
    return f"""Let's think step-by-step.

Feedback: {text}
Step-by-step reasoning:
1. Identify the type of issue.
2. Match it to one of: Bug, Feature Request, Complaint, Compliment, General Feedback.
Now think:
Feedback: {text}
Category:"""

# Run the test
for i, feedback in enumerate(feedbacks[:5]):
    print(f"\n--- Feedback {i+1} ---")
    print("Feedback:", feedback)

    for name, prompt_fn in {
        "Zero-Shot": zero_shot_prompt,
        "Few-Shot": few_shot_prompt,
        "Chain-of-Thought": chain_of_thought_prompt
    }.items():
        prompt = prompt_fn(feedback)
        response = classifier(prompt, max_new_tokens=50, do_sample=False)[0]['generated_text']
        print(f"\n{name} Output:\n", response)
