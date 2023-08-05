import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("DATA\dataset.csv")
st.header("Graphs After Analysis")
st.write("__________________________________")
st.write("")
st.write("")
st.write("")


df = data.drop("Unnamed: 0", axis=1)
df = df.drop_duplicates()
df["duration_ms"]= df["duration_ms"].replace("durations_ms", )

# 1. Top 5 popular artists
popular_artists = df.groupby("artists").count().sort_values(by='popularity', ascending=False)['popularity'][:5]
st.subheader(" Graph 1 - Top 5 popular artists")
fig, ax = plt.subplots()
ax.bar(popular_artists.index, popular_artists.values)
ax.set_xlabel("Artist")
ax.set_ylabel("Popularity")
ax.set_title("Top 5 Popular Artists")
plt.xticks(rotation=45)

# Display the chart using Streamlit
st.pyplot(fig)
st.markdown("&nbsp;")

#2.top 5 longest songs or tracks
long_songs = df[["track_name", "duration_ms"]].sort_values(by="duration_ms", ascending=False)[:5]
st.subheader(" Graph 2 - top 5 longest songs or tracks")
fig, ax = plt.subplots()

ax.barh(long_songs["track_name"], long_songs["duration_ms"] / 1000, color="skyblue")
ax.set_xlabel("Duration (seconds)")
ax.set_ylabel("Song")
ax.set_title("Top 5 Longest Songs")
plt.gca().invert_yaxis()

# Display the graph using Streamlit
st.pyplot(fig)
st.markdown("&nbsp;")
st.markdown("&nbsp;")

#3.
trend_genre = df[["track_genre", "popularity"]].sort_values(by="popularity", ascending=False)[:5]
st.subheader("Graph 3 - Top trending genre")
fig, ax = plt.subplots()
ax.bar(trend_genre["track_genre"], trend_genre["popularity"], color="salmon")
ax.set_xlabel("Genre")
ax.set_ylabel("Popularity")
ax.set_title("Top 5 Trending Genres")
plt.xticks(rotation=45)

# Display the graph using Streamlit
st.pyplot(fig)
st.markdown("&nbsp;")
st.markdown("&nbsp;")


#4.
danceable = df[["track_name", "artists", "danceability"]].sort_values(by="danceability", ascending=False)[:5]
st.subheader("Graph 4 - Top 5 most danceable songs")
fig, ax = plt.subplots()
ax.barh(danceable["track_name"] + " - " + danceable["artists"], danceable["danceability"], color="limegreen")
ax.set_xlabel("Danceability")
ax.set_ylabel("Song - Artist")
ax.set_title("Top 5 Most Danceable Songs")
plt.gca().invert_yaxis()

# Display the graph using Streamlit
st.pyplot(fig)
st.markdown("&nbsp;")
st.markdown("&nbsp;")


#5.
st.set_option('deprecation.showPyplotGlobalUse', False)
st.subheader("Graph 5 - finding correlation between the variables and vizualize it")
numeric_columns = df.select_dtypes(include=[float, int]).columns
df_numeric = df[numeric_columns]
corr_table = df_numeric.corr(method="pearson") #get variables the correlation
corr_table
plt.figure(figsize=(16,4))
sns.heatmap(corr_table, annot=True, fmt=".1g")
plt.title("Correlation Heatmap between variables")
plt.figure(figsize=(16, 4))
sns.heatmap(corr_table, annot=True, fmt=".1g")
plt.title("Correlation Heatmap between variables")

# Display the graph using Streamlit
st.pyplot()

