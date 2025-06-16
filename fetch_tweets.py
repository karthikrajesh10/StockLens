import os
import time
import pandas as pd
import tweepy
from dotenv import load_dotenv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Load environment variables
load_dotenv()
bearer_token = os.getenv("BEARER_TOKEN")


# Define a safe fetch wrapper to handle rate limits
def safe_fetch(client, query, max_results):
    try:
        return client.search_recent_tweets(
            query=query,
            max_results=max_results,
            tweet_fields=['created_at', 'lang', 'text']
        )
    except tweepy.TooManyRequests:
        print("⏳ Rate limit hit. Waiting 15 minutes...")
        time.sleep(15 * 60)
        return safe_fetch(client, query, max_results)


# Fetch tweets with query and save to DataFrame
def fetch_tweets(query, max_results=100):
    client = tweepy.Client(bearer_token=bearer_token)
    response = safe_fetch(client, query, max_results)

    tweet_data = []
    if response.data:
        for tweet in response.data:
            if tweet.lang == 'en':
                tweet_data.append([tweet.created_at, tweet.text])

    df = pd.DataFrame(tweet_data, columns=['Time', 'Tweet'])
    return df


# Main execution
if __name__ == "__main__":
    df = fetch_tweets("nifty OR sensex OR #stockmarket", max_results=50)

    if df.empty:
        print("⚠️ No tweets found.")
    else:
        df.to_csv("tweets.csv", index=False)  # ✅ Save the tweets to a file
        print("✅ Tweets saved to tweets.csv")
        print(df.head())
