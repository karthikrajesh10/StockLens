import schedule
import time
import subprocess

# Define your job to run every X minutes
def job():
    print("🔄 Running scheduled tweet fetch and sentiment analysis...")
    # Run your sentiment fetch and analyze in sequence
    subprocess.run(["python", "fetch_tweets.py"])
    subprocess.run(["python", "analyze_sentiment.py"])

# Schedule the job every 15 minutes (or as needed)
schedule.every(15).minutes.do(job)

# Run scheduler loop
print("🕒 Scheduler started. Press Ctrl+C to exit.")
while True:
    schedule.run_pending()
    time.sleep(1)
