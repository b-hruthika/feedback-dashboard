import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

# Load data
df = pd.read_csv("multilabel_with_urgency.csv")
feedback = df["feedback_text"].tolist()

# Extract keywords using TF-IDF + NMF
vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words="english")
X = vectorizer.fit_transform(feedback)

nmf = NMF(n_components=5, random_state=42)
nmf.fit(X)

# Show topics
feature_names = vectorizer.get_feature_names_out()
for topic_idx, topic in enumerate(nmf.components_):
    top_words = [feature_names[i] for i in topic.argsort()[-10:]]
    print(f"\n🧠 Topic #{topic_idx + 1}: {' | '.join(top_words)}")
