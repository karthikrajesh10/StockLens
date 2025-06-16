import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to calculate sentiment and compound score
def get_sentiment_info(text):
    score = analyzer.polarity_scores(text)
    compound = score['compound']
    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment, compound

# Process tweet data that doesn't have sentiment columns yet
def process_tweet_data(tweet_file):
    tweet_df = pd.read_csv(tweet_file)

    if 'Sentiment' not in tweet_df.columns or 'CompoundScore' not in tweet_df.columns:
        # Analyze tweets only if sentiment info is missing
        sentiments, scores = zip(*tweet_df['Tweet'].apply(get_sentiment_info))
        tweet_df['Sentiment'] = sentiments
        tweet_df['CompoundScore'] = scores

    tweet_df.rename(columns={'Tweet': 'Text'}, inplace=True)
    tweet_df['Source'] = 'Tweet'
    return tweet_df[['Time', 'Text', 'Sentiment', 'CompoundScore', 'Source']]

# Load and clean news data
def process_news_data(news_file):
    news_df = pd.read_csv(news_file)
    if 'Source' not in news_df.columns:
        news_df['Source'] = 'News'
    return news_df[['Time', 'Text', 'Sentiment', 'CompoundScore', 'Source']]

# Combine both sources
def combine_sentiment_data(tweet_file, news_file):
    tweet_df = process_tweet_data(tweet_file)
    news_df = process_news_data(news_file)

    combined_df = pd.concat([tweet_df, news_df], ignore_index=True)
    combined_df.sort_values(by='Time', ascending=False, inplace=True)
    return combined_df

# Main
if __name__ == "__main__":
    tweet_file = "tweets.csv"
    news_file = "news_sentiment.csv"

    final_df = combine_sentiment_data(tweet_file, news_file)
    final_df.to_csv("sentiment_analysed.csv", index=False)

    print("✅ Combined sentiment saved to sentiment_analysed.csv")
    print(final_df.head())
