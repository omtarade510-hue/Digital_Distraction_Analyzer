import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("digital_behavior.csv")

st.title("📱 Digital Distraction Analyzer")

st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

st.subheader("⏱ Daily Screen Time (hrs)")
st.bar_chart(df["daily_screen_time_hrs"])

st.subheader("📱 Social Media Usage (hrs)")
st.line_chart(df["social_media_hrs"])

st.subheader("🔔 Notifications per Day")
st.bar_chart(df["notifications_per_day"])

st.subheader("😴 Sleep Hours")
st.line_chart(df["sleep_hrs"])

st.subheader("📈 Productivity Score")
st.bar_chart(df["productivity_score"])

st.subheader("🔗 Correlation Matrix")
st.write(df.corr(numeric_only=True))
