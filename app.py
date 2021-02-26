import streamlit as st
import datetime
import requests
import pandas as pd
import numpy as np


'''
# TaxiFareModel front
'''

st.markdown("""# Your Taxifare Predictor""")

## API ENDPOINT
url = 'http://taxifare.lewagon.ai/predict_fare/'

# SET INPUT VARIABLES
d = st.date_input("pickupdate", datetime.date(2019, 7, 6))

t = st.time_input('pickuptime', datetime.time(8, 45))

pickup_datetime = (f'{d} {t} UTC')
pickup_longitude = st.number_input('pickup longitude')
pickup_latitude = st.number_input('pickup latitude')
dropoff_longitude = st.number_input('dropoff longitude')
dropoff_latitude = st.number_input('dropoff latitude')
passenger_count = st.selectbox('Number of passengers', list(range(1,20)))

## 2. Let's build a dictionary containing the parameters for our API...
params = dict(
  key='2012-10-06 12:10:20.0000001',
  pickup_datetime=pickup_datetime,
  pickup_longitude=pickup_longitude,
  pickup_latitude=pickup_latitude,
  dropoff_longitude=dropoff_longitude,
  dropoff_latitude=passenger_count,
  passenger_count=passenger_count
)

## 3. Let's call our API using the `requests` package...
response = requests.get(url, params=params).json()

## 4. Let's retrieve the prediction from the **JSON** returned by the API...
pred = response["prediction"]

## Finally, we can display the prediction to the user
st.markdown(f"Your predicted taxi fare: {round(pred, 2)} Pesos")

