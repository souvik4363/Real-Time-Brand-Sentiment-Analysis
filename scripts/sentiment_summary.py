import pandas as pd

df = pd.read_csv("data/apple_news_with_sentiment.csv")

# Count sentiment distribution
sentiment_counts = df["Sentiment"].value_counts()
print("Sentiment Distribution:")
print(sentiment_counts)
# Calculate percentages
sentiment_percentages = (sentiment_counts / sentiment_counts.sum()) * 100
print("\nSentiment Percentages:")
print(sentiment_percentages)
