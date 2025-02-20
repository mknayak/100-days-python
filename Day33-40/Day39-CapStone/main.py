from data_manager import DataManager
from notification_manager import NotificationManager
from flight_data import FlightData
from flight_search import  FlightSearch
from datetime import datetime, timedelta
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
notification_manager = NotificationManager()
better_deal_found=False
flight_search=FlightSearch()


def update_city_codes(cities):
    if len(cities) > 0:
        for city in cities:
            city_ids = flight_search.city_search(city["city"])
            if len(city_ids) > 0:
                data_manager.update_city(city['id'], city_ids[0])

#Get all deals from Google sheet
cities = data_manager.get_deals()
missing_code_cities = [n for n in cities if n["iataCode"] == ""]
#update_city_codes(missing_code_cities)

valid_cities= [n for n in cities if n["iataCode"] != ""]
source_city_code= flight_search.city_search("BENGALURU")
if len(source_city_code) > 0:
    source=source_city_code[0]
    for vc in valid_cities:
        travel_date= datetime.today()+ timedelta(days=30*6)
        return_date = travel_date+ timedelta(days=10)
        destination=vc["iataCode"]
        itenaries = flight_search.price_search(source, destination, travel_date, return_date)
        if len(itenaries) > 0:
            pricelist= [n.price for n in itenaries if n.price < vc["lowestPrice"]]
            if len(pricelist) > 0:
                notification_manager.send_sms_notification(f"Cheap flight found. {source} to {destination} at {pricelist[0]} ")


if better_deal_found:
    notification_manager.send_sms_notification("Hello")

