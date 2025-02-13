import requests
from twilio.rest import Client
API="https://api.openweathermap.org/data/2.5/weather"
API_WEATHER_FORECAST="https://api.openweathermap.org/data/2.5/forecast"
API_KEY="dd312b060505c0040f1c7923fbd89885"
LATITUDE=1.352083
LONGITUDE=103.819839
CNT=40 #no of items in list. max 0-40
params={
    "appid": API_KEY,
    "lat":LATITUDE,
    "lon":LONGITUDE,
    "cnt":CNT
}
def send_sms_notification(message):
    account_sid = 'AC93de7bcd904c80a1b17474e2c7bfa1d0'
    auth_token = 'd1d68290f0698d32c43f679be3de39e1'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='MG18e357cd6901aa14be928a520b533856',
        body= message,
        to='+6583992760'
    )
    print(message.sid)

def send_whatapp_notification(message):
    phone_number_id="552588537940270"
    access_token="EAAc2bs4BsTMBO6mZCgZCDwtYEKvprVSNy9HZCZCYfZBQ4jucqwCrxZAZBP5L4jlT89tJyID19tBee5GDUulj0LJrZBvCWlVxJ0aiHFb16yl2gSp1l5oxWg265kuQNSuRMsOpysjeqt25PyLgRA8RCRbc3sKkUuZBB3trtXNZBdPxj7RS5TjFEQ6UrN13IY9DUYLtWiS3tkv3v2UDFaS4PtaLWrbz72"
    api=f"https://graph.facebook.com/v21.0/{phone_number_id}/messages"
    content=    {
                    "messaging_product": "whatsapp",
                    "to": "+6583992760",
                    "type": "text",
                    "text": {
                        "body": message
                    }
                }
    headers = { "Content-Type": "application/json", "Authorization": "Bearer " + access_token }
    response = requests.post(api,headers=headers, json=content)
    print(response.text)

def get_next_weather_forecast():
    response = requests.get(API_WEATHER_FORECAST,params=params)
    return response.json()
data = get_next_weather_forecast()
will_rain=False
for wc in data["list"]:
    weather=wc["weather"][0]
    if weather["id"] <700:
        will_rain=True
        print(f"It's going to rain around '{wc["dt_txt"]}'")
        break

if not will_rain:
    print("It's NOT going to rain")

#Slice method
rain_data_list=[{"time":wc["dt_txt"],"weather":wc["weather"]} for wc in data["list"] if wc["weather"][0]["id"] <700]
if len(rain_data_list)>0:
    #send_sms_notification(f"It's going to rain at {rain_data_list[0]["time"]}")
    send_whatapp_notification(f"It's going to rain at {rain_data_list[0]["time"]}")
else:
    print("It's NOT going to rain")
