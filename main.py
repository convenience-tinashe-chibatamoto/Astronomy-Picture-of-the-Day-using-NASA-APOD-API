import requests
import streamlit as st
import os
from datetime import datetime, timedelta

# Prepare API key and API url
api_key = os.getenv("API_KEY")
url = "https://api.nasa.gov/planetary/apod?"

# Create a date input widget in the sidebar
date = st.sidebar.date_input('Select a date', datetime.now(), max_value=datetime.now())

# Check if the selected date is in the future
if date > datetime.now():
    st.error('Future dates are not allowed. Please select a valid date.')
else:
    # Convert the date to string format
    date_str = date.strftime('%Y-%m-%d')

    # Get the request data as a dictionary
    response1 = requests.get(f"{url}date={date_str}&api_key={api_key}")
    data = response1.json()

    # Extract the image title, url and, explanation
    title = data["title"]
    image_url = data["url"]
    explanation = data["explanation"]

    # Download the image
    image_filepath = "img.png"
    response2 = requests.get(image_url)
    with open(image_filepath, 'wb') as file:
        file.write(response2.content)

    st.title(title)
    st.image(image_filepath)
    st.write(explanation)
