import streamlit as st
import datetime
import requests
import pandas as pd
import numpy as np

st.markdown("""# Your Taxifare Predictor""")

## API ENDPOINT
url = 'http://taxifare.lewagon.ai/predict_fare/'

# SET INPUT VARIABLES
d = st.date_input("pickupdate", datetime.date(2019, 7, 6))

t = st.time_input('pickuptime', datetime.time(8, 45))

pickup_datetime = (f'{d} {t} UTC')
pickup_longitude = st.number_input('pickup longitude', format="%.5f")
pickup_latitude = st.number_input('pickup latitude', format="%.5f")
dropoff_longitude = st.number_input('dropoff longitude', format="%.5f")
dropoff_latitude = st.number_input('dropoff latitude', format="%.5f")
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
def api(url,params):
    print("api requested")
    response = requests.get(url, params=params).json()
    ## 4. Let's retrieve the prediction from the **JSON** returned by the API...
    pred = response["prediction"]
    ## Finally, we can display the prediction to the user
    st.markdown(f"""# Your predicted taxi fare: {round(pred, 2)} Pesos""")

api(url,params)

@st.cache
def get_map_data():
    print('get_map_data called')
    return pd.DataFrame(
            [[pickup_latitude, pickup_longitude]],
            columns=['lat', 'lon']
        )

# if st.checkbox('Show map', False):
#     df = get_map_data()

st.map(get_map_data())
# image = Image.open('images/map.png')
# st.image(image, caption='map', use_column_width=False)