import snscrape.modules.twitter as sntwitter
import pandas as pd

def scrape_tweets(query, limit=50):
    tweets_list = []

    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= limit:
            break
        tweets_list.append([tweet.date, tweet.id, tweet.content])

    df = pd.DataFrame(tweets_list, columns=['Time', 'Tweet ID', 'Text'])
    df.to_csv('tweets_scraped.csv', index=False)
    print(f"✅ Scraped {len(df)} tweets and saved to tweets_scraped.csv")

if __name__ == "__main__":
    scrape_tweets("nifty OR sensex OR #stockmarket lang:en since:2025-06-01 until:2025-06-12", limit=50)
