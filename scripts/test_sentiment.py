from textblob import TextBlob
text = "Apple products are amazing"
blob = TextBlob(text)
print(blob.sentiment)