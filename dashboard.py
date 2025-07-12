import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="Feedback Dashboard", layout="wide")
st.title("📊 User Feedback Dashboard")

# Load your data
df = pd.read_csv("scored_feedback.csv", parse_dates=["timestamp"], encoding="ISO-8859-1")

st.write("Sample Feedback Texts:")
st.write(df["feedback_text"].head(10))

# Ensure feedback_text is always a plain string
df["feedback_text"] = df["feedback_text"].astype(str)


# Show raw data
st.subheader("📋 All Feedback")
st.dataframe(df)

# Category-wise Feedback Count
st.subheader("📂 Category-wise Feedback Count")
category_counts = df["manual_category"].value_counts()
st.bar_chart(category_counts)

# Optional Pie Chart
fig1, ax1 = plt.subplots()
ax1.pie(category_counts, labels=category_counts.index, autopct="%1.1f%%", startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)
# Sidebar filters
st.sidebar.header("🔍 Filter Feedback")

# Filter by source
source_filter = st.sidebar.multiselect("Select Sources:", df["source"].unique(), default=df["source"].unique())

# Filter by sentiment
sentiment_filter = st.sidebar.multiselect("Select Sentiment:", df["sentiment"].unique(), default=df["sentiment"].unique())

# Filter by category
category_filter = st.sidebar.multiselect("Select Categories:", df["manual_category"].unique(), default=df["manual_category"].unique())

# Keyword search
search_term = st.sidebar.text_input("Search in feedback text:")

# Date range filter
start_date = st.sidebar.date_input("Start Date", df["timestamp"].min().date())
end_date = st.sidebar.date_input("End Date", df["timestamp"].max().date())

# Apply filters
filtered_df = df[
    (df["timestamp"].dt.date >= start_date) &
    (df["timestamp"].dt.date <= end_date) &
    df["source"].isin(source_filter) &
    df["sentiment"].isin(sentiment_filter) &
    df["manual_category"].isin(category_filter)
]

if search_term:
    search_matches = df[df["feedback_text"].astype(str).str.contains(search_term, case=False, na=False)]
    st.write(f"Debug: Found {len(search_matches)} matches")
    st.write(search_matches[["timestamp", "feedback_text"]].head())
    filtered_df = filtered_df[filtered_df["feedback_text"].str.contains(search_term, case=False, na=False)]



# Show filtered data
st.write(f"Showing {len(filtered_df)} results")
st.dataframe(filtered_df)

# Download button for filtered results
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Filtered Feedback as CSV",
    data=csv,
    file_name="filtered_feedback.csv",
    mime="text/csv"
)

st.subheader("📈 Sentiment Trend Over Time")
sentiment_trend = (
    df.set_index("timestamp")
      .groupby([pd.Grouper(freq="W"), "sentiment"])
      .size()
      .unstack()
      .fillna(0)
)
st.line_chart(sentiment_trend)
st.subheader("🧁 Category Distribution")

fig2, ax2 = plt.subplots()
category_counts = df["manual_category"].value_counts()
ax2.pie(category_counts, labels=category_counts.index, autopct="%1.1f%%")
ax2.axis("equal")
st.pyplot(fig2)
st.subheader("🚨 Weekly Average Urgency Score")

weekly_urgency = df.set_index("timestamp").resample("W")["urgency_score"].mean()
st.line_chart(weekly_urgency)
st.subheader("🚨 Weekly Alert Summary")

# Example logic — tweak as needed
latest_week = df["timestamp"].max().to_period("W")
weekly_data = df[df["timestamp"].dt.to_period("W") == latest_week]

neg_count = len(weekly_data[weekly_data["sentiment"] == "Negative"])
bug_count = len(weekly_data[weekly_data["manual_category"].str.contains("bug", case=False, na=False)])
high_urgency = len(weekly_data[weekly_data["urgency_score"] > 0.8])

if bug_count > 5 or high_urgency > 5 or neg_count > 10:
    st.error("⚠️ Critical Alert: Negative sentiment or bugs spiked this week!")
else:
    st.success("✅ All good! No critical spikes detected in latest feedback.")


