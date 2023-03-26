import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Define the API endpoint for air quality data
AQ_URL = "https://api.openaq.org/v1/latest?country=BD"

# Fetch air quality data from the API
data = requests.get(AQ_URL).json()
results = data['results']

# Convert data to Pandas DataFrame
aq_df = pd.json_normalize(results)
coordinates = pd.json_normalize(aq_df['coordinates'])
aq_df = pd.concat([aq_df, coordinates], axis=1)

# Plot the data
fig, ax = plt.subplots()
ax.scatter(aq_df['longitude'], aq_df['latitude'], c=aq_df['measurements.value'], cmap='Reds')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Air Quality in Bangladesh')
st.pyplot(fig)
