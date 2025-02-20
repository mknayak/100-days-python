import requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.api_endpoint="https://api.sheety.co/9769300c2cb0b0ac26f71741c7dfcf00/flightDeals/prices"
        self.auth_token="askdKNKDLASOIJklja8897HJJKHAKHS77a8hn3qmkao9932q189h"

    def get_deals(self):
        response = requests.get(self.api_endpoint, headers={"Authorization": "Bearer " + self.auth_token})
        json_data = response.json()
        all_deals = json_data["prices"]
        print(json_data)
        return all_deals

    def update_city(self,row_index,code):
        api_endpoint=f"{self.api_endpoint}/{row_index}"
        api_data={"price":{'iataCode':code}}
        response = requests.put(api_endpoint, json=api_data, headers={"Authorization": "Bearer " + self.auth_token})
        pass
