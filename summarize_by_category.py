import pandas as pd, json
from transformers import pipeline

summarizer = pipeline("summarization", model="Falconsai/text_summarization")
df = pd.read_csv("scored_feedback.csv")

summaries = {}
for category in ["Bug","Complaint","Feature Request","Compliment","General Feedback"]:
    texts = df[df[category]==1]["feedback_text"].tolist()
    if not texts: 
        summaries[category] = "No items."
        continue
    joined = " ".join(texts)[:2000]  # 2k char cap
    summaries[category] = summarizer(joined, max_length=60,
                                     min_length=15, do_sample=False)[0]["summary_text"]

with open("category_summaries.json","w") as f:
    json.dump(summaries, f, indent=2)

print("✅ Summaries saved -> category_summaries.json")
