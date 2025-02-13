import time

import requests
import json
import datetime

API ="https://api.sunrise-sunset.org/json"
ISS_API="http://api.open-notify.org/iss-now.json"
LATITUDE=1.352083
LONGITUDE=103.819839

def is_iss_overhead():
    response = requests.get(ISS_API)
    print(response.json())
    iss_lat=response.json()["iss_position"]["latitude"]
    iss_long=response.json()["iss_position"]["longitude"]
    if LATITUDE-5 <= iss_lat <= LATITUDE+5 and LONGITUDE - 5 <= iss_long <= LONGITUDE + 5:
        return True


def is_nighttime():
    api_params={
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "formatted":0
    }
    response = requests.get(API, params=api_params)
    res_data= response.json()
    sunrise = res_data['results']['sunrise']
    sunset = res_data['results']['sunset']
    if sunrise > datetime.datetime.now().hour > sunset:
        return True

while True:

    if is_iss_overhead() and is_nighttime():
        print("ISS is overhead")

