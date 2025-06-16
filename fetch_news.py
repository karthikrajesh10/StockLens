import os
import requests
import pandas as pd
from dotenv import load_dotenv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load API key
load_dotenv()
news_api_key = os.getenv("NEWS_API_KEY")

# Sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = analyzer.polarity_scores(text)
    compound = score["compound"]
    if compound >= 0.05:
        return "Positive", compound
    elif compound <= -0.05:
        return "Negative", compound
    else:
        return "Neutral", compound

def fetch_news(query="Indian stock market", page_size=20):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": "en",
        "pageSize": page_size,
        "sortBy": "publishedAt",
        "apiKey": news_api_key,
        "domains": "moneycontrol.com,economictimes.indiatimes.com,livemint.com,financialexpress.com"
    }
    response = requests.get(url, params=params)
    articles = response.json().get("articles", [])

    news_data = []
    for article in articles:
        title = article["title"]
        published_at = article["publishedAt"]
        sentiment, compound = get_sentiment(title)
        news_data.append([published_at, title, sentiment, compound, "News"])

    return pd.DataFrame(news_data, columns=["Time", "Text", "Sentiment", "CompoundScore", "Source"])

if __name__ == "__main__":
    df = fetch_news("nifty OR sensex OR Indian stock market", page_size=20)
    df.to_csv("news_sentiment.csv", index=False)
    print("✅ News sentiment saved to news_sentiment.csv")
    print(df.head())
