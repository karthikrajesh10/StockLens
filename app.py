import streamlit as st
import pandas as pd
import altair as alt

# Load CSV
@st.cache_data
def load_data():
    df = pd.read_csv("sentiment_analysed.csv", parse_dates=["Time"])
    df.dropna(subset=['Text', 'Sentiment', 'CompoundScore'], inplace=True)
    return df

# Page settings
st.set_page_config(page_title="StockLens: Sentiment Dashboard", layout="wide")

st.title("📈 StockLens – Stock Market Sentiment Analyzer")
st.caption("Get real-time insights from Tweets & News related to Indian Stock Market")

# Load and preview data
df = load_data()
st.write(f"📦 Loaded {len(df)} records")

# Sidebar filters
st.sidebar.header("🔍 Filter")
source_filter = st.sidebar.multiselect("Select Source", options=["Tweet", "News"], default=["Tweet", "News"])
sentiment_filter = st.sidebar.multiselect("Select Sentiment", options=["Positive", "Neutral", "Negative"], default=["Positive", "Neutral", "Negative"])

# Apply filters
filtered_df = df[df['Source'].isin(source_filter)]
filtered_df = filtered_df[filtered_df['Sentiment'].isin(sentiment_filter)]

# Show filtered data
st.subheader("🔎 Filtered Sentiment Data")
st.dataframe(filtered_df.sort_values("Time", ascending=False), use_container_width=True, height=400)

# Sentiment counts
st.subheader("📊 Sentiment Distribution")
sentiment_counts = filtered_df['Sentiment'].value_counts().reset_index()
sentiment_counts.columns = ['Sentiment', 'Count']
chart = alt.Chart(sentiment_counts).mark_bar().encode(
    x=alt.X('Sentiment', sort='-y'),
    y='Count',
    color='Sentiment'
)
st.altair_chart(chart, use_container_width=True)

# Line chart of sentiment over time
st.subheader("📉 Compound Score Over Time")
line_chart = alt.Chart(filtered_df).mark_line(point=True).encode(
    x='Time:T',
    y='CompoundScore:Q',
    color='Source'
).properties(height=300)
st.altair_chart(line_chart, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit · Powered by VADER · Built by [Karthik](#)")

