import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style="whitegrid")

# Load CSV
df = pd.read_csv("sentiment_analysed.csv")

# Convert Time to datetime safely (handles mixed formats)
df['Time'] = pd.to_datetime(df['Time'], format='mixed', errors='coerce')
df.dropna(subset=['Time'], inplace=True)  # Drop rows with invalid dates

# 1. Pie Chart: Sentiment distribution
def plot_sentiment_distribution():
    plt.figure(figsize=(6, 6))
    sentiment_counts = df['Sentiment'].value_counts()
    plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title("Sentiment Distribution")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()

# 2. Line Plot: Sentiment score over time
def plot_sentiment_over_time():
    plt.figure(figsize=(12, 6))
    df_sorted = df.sort_values(by='Time')
    sns.lineplot(data=df_sorted, x='Time', y='CompoundScore', hue='Source', marker="o")
    plt.title("Sentiment Score Over Time")
    plt.xlabel("Time")
    plt.ylabel("Compound Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 3. Bar Chart: Average sentiment score by source
def plot_avg_score_by_source():
    plt.figure(figsize=(8, 5))
    avg_scores = df.groupby('Source')['CompoundScore'].mean().reset_index()
    sns.barplot(data=avg_scores, x='Source', y='CompoundScore', palette='viridis')
    plt.title("Average Sentiment Score by Source")
    plt.ylabel("Avg. Compound Score")
    plt.ylim(-1, 1)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("📊 Generating sentiment visualizations...")
    plot_sentiment_distribution()
    plot_sentiment_over_time()
    plot_avg_score_by_source()
    print("✅ Visualizations completed.")
