import requests
from datetime import datetime
from flight_data import FlightData
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.email="frills_wait_9j@icloud.com"
        self.password="M@n@s0000"
        self.api_key="rjyPFlwrIAsmGEGia1vOAargVGeqqyN7"
        self.api_secret="AyiB7xvVfGK0TNbQ"
        self.base_url="https://test.api.amadeus.com"
        self.access_token=self.authenticate()


    def authenticate(self):
        auth_endpoint=f"{self.base_url}/v1/security/oauth2/token"
        auth_header={"Content-Type":"application/x-www-form-urlencoded"}
        auth_params=f"grant_type=client_credentials&client_id={self.api_key}&client_secret={self.api_secret}"

        auth_response = requests.post(auth_endpoint, headers=auth_header, data=auth_params).json()
        access_token=auth_response["access_token"]
        return access_token

    def city_search(self, destination_city):
        flight_search_endpoint=f"{self.base_url}/v1/reference-data/locations"
        flight_search_header={"Content-Type":"application/json","Authorization":"Bearer "+self.access_token}
        flight_search_params={"subType":"CITY", "keyword":destination_city, "page[limit]":2}

        flight_search_response= requests.get(flight_search_endpoint, headers=flight_search_header, params=flight_search_params)
        api_response=flight_search_response.json()
        cities= [n['iataCode'] for n in api_response["data"]]
        print(cities)
        return cities

    def price_search(self,source, destination_city, travel_date:datetime,return_date:datetime):
        flight_search_endpoint=f"{self.base_url}/v2/shopping/flight-offers"
        flight_search_params={"originLocationCode":source,
                              "destinationLocationCode":destination_city,
                              "departureDate":travel_date.strftime("%Y-%m-%d"),
                              "returnDate":return_date.strftime("%Y-%m-%d"),
                              "adults":1,"max":20}
        flight_search_header={"Content-Type":"application/json","Authorization":"Bearer "+self.access_token}
        response=requests.get(flight_search_endpoint, headers=flight_search_header, params=flight_search_params)
        api_response=response.json()["data"]
        flight_data_list=[]
        for flight in api_response:
            fd=FlightData(source,destination_city,flight["price"])
            flight_data_list.append(fd)

        return flight_data_list




