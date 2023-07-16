import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

data = pd.read_csv("DATA\dataset.csv")

df = data.drop("Unnamed: 0", axis=1)
df = df.drop_duplicates()
df["duration_ms"]= df["duration_ms"].replace("durations_ms", )

popular_artists = df.groupby("artists").count().sort_values(by='popularity', ascending=False)['popularity'][:5]
st.subheader(" Graph ")
fig, ax = plt.subplots()
ax.bar(popular_artists.index, popular_artists.values)
ax.set_xlabel("Artist")
ax.set_ylabel("Popularity")
ax.set_title("Top 5 Popular Artists")
plt.xticks(rotation=45)

# Display the chart using Streamlit
st.pyplot(fig)
