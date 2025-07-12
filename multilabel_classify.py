import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import f1_score


# 1) Load the data you already have
df = pd.read_csv("final_feedback_data.csv", encoding="windows-1252")



# 2) Map each manual_category to a list  (for now most rows have 1 label)
df["label_list"] = df["manual_category"].apply(lambda x: [x])

# 3) Encode labels -> binary vectors
mlb = MultiLabelBinarizer()
y = mlb.fit_transform(df["label_list"])

# 4) Convert feedback text to embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")          # tiny & fast
X = model.encode(df["feedback_text"].tolist(), show_progress_bar=True)

from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression

clf = OneVsRestClassifier(LogisticRegression(max_iter=500))
clf.fit(X, y)


# 5) Train a simple One‑vs‑Rest logistic model
clf = OneVsRestClassifier(LogisticRegression(max_iter=500))
clf.fit(X, y)

# Confidence scoring
probas = clf.predict_proba(X)
df["confidence_score"] = probas.max(axis=1)

# 6) Predict multi‑labels (YES/NO per class)
y_pred = clf.predict(X)
# 6.1) Get max confidence score for each prediction
probas = clf.predict_proba(X)  # get probability values
df["confidence_score"] = probas.max(axis=1)  # max confidence for each row

# 7) Attach predictions back to dataframe
df_preds = pd.DataFrame(y_pred, columns=mlb.classes_)

df_final = pd.concat([df, df_preds], axis=1)  # df already includes confidence_score


df_final.to_csv("multilabel_feedback.csv", index=False)

# 8) Metrics
print("Macro‑F1:", f1_score(y, y_pred, average='macro'))
