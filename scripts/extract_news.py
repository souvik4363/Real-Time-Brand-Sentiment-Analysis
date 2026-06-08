import os
import requests
import pandas as pd
from dotenv import load_dotenv

#load.env file
load_dotenv()

#get Api key
Api_key=os.getenv("News_API_Key")

#Brand name
brand = "Apple"

# Api url
url = f"https://newsapi.org/v2/everything?q={brand}&language=en&apikey={Api_key}"

#Request data
response = requests.get(url)
# convert tojson
data = response.json()

print("Status:", response.status_code)
print("Total Articles:", data.get("totalResults", 0))

articles = []
for article in data.get("articles", []):
    articles.append({
        "source": article["source"]["name"],
        "author": article["author"],
        "title": article["title"],
        "description": article["description"],
        "url": article["url"],
        "publishedAt": article["publishedAt"]
    })

df = pd.DataFrame(articles)
print(df.head())

df.to_csv("data/apple_news.csv", index=False)

print("Csv file created successfully.")