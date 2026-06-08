import pandas as pd
from textblob import TextBlob
# Load the news data
df = pd.read_csv("data/apple_news.csv")
# Function to analyze sentiment
def get_sentiment(text):
    if pd.isna(text):
        return "Neutral"
    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
    
    #Create Sentiment coloumn
df["Sentiment"] = df["title"].apply(get_sentiment)

#Show first 5 rows
print(df[["title", "Sentiment"]].head())
#Save new file
df.to_csv("data/apple_news_with_sentiment.csv", index=False)
print("Sentiment analysis completed and saved to apple_news_with_sentiment.csv")
    