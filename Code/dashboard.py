import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Digital Distraction Analyzer", layout="wide")

# Title
st.title("📱 Digital Distraction Analyzer Dashboard")
st.write("Analysis of digital behavior and productivity using synthetic data")

# Load data
df = pd.read_csv(
    "digital_behavior.csv"
)

# Sidebar
st.sidebar.header("Filter Options")

# Age filter
age_range = st.sidebar.slider(
    "Select age Range",
    int(df["age"].min()),
    int(df["age"].max()),
    (18, 30)
)

filtered_df = df[
    (df["age"] >= age_range[0]) &
    (df["age"] <= age_range[1])
]

# Show dataset
st.subheader("📄 Dataset Preview")
st.dataframe(filtered_df.head(20))

# Key metrics
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Screen Time (hrs)",
    round(filtered_df["daily_screen_time_hrs"].mean(), 2)
)

col2.metric(
    "Average Notifications / Day",
    int(filtered_df["notifications_per_day"].mean())
)

col3.metric(
    "Average Productivity Score",
    round(filtered_df["productivity_score"].mean(), 2)
)

# Scatter plot: Screen Time vs Productivity
st.subheader("📉 Screen Time vs Productivity")

fig1, ax1 = plt.subplots()
sns.scatterplot(
    x="daily_screen_time_hrs",
    y="productivity_score",
    data=filtered_df,
    ax=ax1
)
ax1.set_xlabel("daily_screen_time_hrs")
ax1.set_ylabel("productivity_score")

st.pyplot(fig1)

# Box plot: Notifications
st.subheader("📦 Notifications Distribution")

fig2, ax2 = plt.subplots()
sns.boxplot(
    y="notifications_per_day",
    data=filtered_df,
    ax=ax2
)

st.pyplot(fig2)

# Correlation heatmap
st.subheader("🔥 Correlation Heatmap")

numeric_df = filtered_df.select_dtypes(include="number")

fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    ax=ax3
)

st.pyplot(fig3)

# Conclusion
st.subheader("✅ Conclusion")
st.write("""
- Higher screen time generally reduces productivity  
- Notifications are a major source of distraction  
- Balanced digital usage improves productivity  
""")
