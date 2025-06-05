import pandas as pd
from transformers import pipeline
import os

# Load raw data
input_path = r"C:\Users\Shib\Documents\Financial-News-Sentiment-Project\data\raw_analyst_ratings.csv\raw_analyst_ratings.csv"
df = pd.read_csv(input_path)

# Load sentiment model
sentiment_pipeline = pipeline("sentiment-analysis")
# Apply model to each headline
df["sentiment_result"] = df["headline"].apply(sentiment_pipeline)
df["Sentiment_Label"] = df["sentiment_result"].apply(lambda x: x[0]['label'])
df["Sentiment_Score"] = df["sentiment_result"].apply(lambda x: x[0]['score'])

# Map labels to signed scores: POSITIVE → +score, NEGATIVE → -score
df["Sentiment_Score"] = df.apply(
    lambda row: row["Sentiment_Score"] if row["Sentiment_Label"] == "POSITIVE" else -row["Sentiment_Score"],
    axis=1
)

# Format the date and remove time zone
df["date"] = pd.to_datetime(df["date"]).dt.date

# Save sentiment data
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/sentiment_with_scores.csv", index=False)
print("✅ Sentiment scores saved to data/processed/sentiment_with_scores.csv")
