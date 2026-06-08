import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("data/apple_news_with_sentiment.csv")

# Count sentiment distribution

sentiment_counts = df["Sentiment"].value_counts()
# Plotting



plt.figure(figsize=(8, 6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%")
plt.title("Sentiment Distribution of Apple News Articles")
plt.savefig("dashboard/sentiment_distribution.png")
plt.show()
