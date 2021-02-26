import streamlit as st
import datetime
import requests


'''
# TaxiFareModel front
'''

st.markdown("""# Your Taxifare Predictor""")

## API ENDPOINT
url = 'http://taxifare.lewagon.ai/predict_fare/'

# SET INPUT VARIABLES
pickup_datetime = st.date_input(
            "Pickup date",
            datetime.date(today))
pickup_longitude = st.number_input('pickup longitude')
pickup_latitude = st.number_input('pickup latitude')
dropoff_longitude = st.number_input('dropoff longitude')
dropoff_latitude = st.number_input('dropoff latitude')
passenger_count = st.selectbox('Number of passengers', list(range(1,20)))

## 2. Let's build a dictionary containing the parameters for our API...
params = {
        "key": '2012-10-06 12:10:20.0000001',
        "pickup_datetime": [float(pickup_datetime)],
        "pickup_longitude": [float(pickup_longitude)],
        "pickup_latitude": [float(pickup_latitude)], 
        "dropoff_longitude": float(dropoff_longitude)], 
        "dropoff_latitude": [float(dropoff_latitude)], 
        "passenger_count": [int(passenger_count)]
        })

## 3. Let's call our API using the `requests` package...
response = requests(url, params=params)

## 4. Let's retrieve the prediction from the **JSON** returned by the API...
pred = response["prediction"]

## Finally, we can display the prediction to the user
st.markdown(f"Your predicted taxi fare: {round(pred, 2)} Pesos")

