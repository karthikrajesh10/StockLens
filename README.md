https://stocklens-jvcrdrxcj7opdbna3kkkzc.streamlit.app/ - Deployment Link


Here's a well-structured and professional **README** file for your **StockLens** project:

---

# 📊 StockLens – AI-Powered Stock Sentiment Analyzer

StockLens is an AI-driven sentiment analysis tool that aggregates and analyzes real-time tweets and news articles related to the **Indian stock market**, helping retail investors gain insights into market mood.

> 🚀 Built using Python · Streamlit · VADER Sentiment Analysis · Tweepy · NewsAPI

---

## 🔍 Features

* 🔁 **Real-Time Tweet & News Fetching**
  Pulls latest tweets (via Tweepy) and news articles (via NewsAPI) about keywords like *Nifty, Sensex*, and *#stockmarket*.

* 🧠 **Sentiment Analysis with VADER**
  Performs compound scoring and classifies text into *Positive, Negative,* or *Neutral* sentiment.

* 📈 **Streamlit Dashboard**
  Visualizes sentiment trends over time, including:

  * Sentiment distribution bar charts
  * Compound score time-series plot
  * Source-based filtering (Tweet vs News)

* 💾 **Persistent Data**
  Merges newly fetched data with existing CSVs while avoiding duplication.

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python, Pandas
* **APIs**: Twitter API (via Tweepy), NewsAPI
* **NLP**: VADER Sentiment Analyzer

---

## 📁 Project Structure

```
stocklens/
│
├── fetch_tweets.py           # Fetch tweets and update tweets.csv
├── fetch_news.py             # Fetch news and save to news_sentiment.csv
├── analyze_sentiment.py      # Combine tweet/news CSVs, perform sentiment analysis
├── app.py                    # Streamlit dashboard
│
├── tweets.csv                # Raw tweet data
├── news_sentiment.csv        # Raw news sentiment data
├── sentiment_analysed.csv    # Final combined sentiment dataset
│
├── .env                      # API keys
└── requirements.txt
```

---

## 🧪 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/stocklens.git
cd stocklens
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up `.env` file**

```
BEARER_TOKEN=your_twitter_bearer_token
NEWS_API_KEY=your_newsapi_key
```

4. **Run the app**

```bash
streamlit run app.py
```

---

## 📊 Sample Dashboard

![Streamlit Dashboard](https://your-image-link.com/dashboard.png)

---

## 🧠 Future Enhancements

* Keyword-specific filtering (e.g., “Reliance” or “Infosys”)
* Dashboard auto-refresh with scheduler
* Historical sentiment tracking
* Stock price overlay with sentiment

---

## 👨‍💻 Author

**Karthik R S**
`22BCE8794` | BTech CSE @ VIT-AP
Passionate about AI, fintech, and meaningful data visualizations.

---

Let me know if you want to include [GIFs or screenshots](f), [GitHub Actions CI for data update](f), or [deployment via Streamlit Cloud or Hugging Face Spaces](f).

