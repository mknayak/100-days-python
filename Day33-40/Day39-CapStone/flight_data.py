
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,source,destination,api_response):
        self.source=source
        self.destination=destination
        self.price=float(api_response["total"])
        self.currency=api_response["currency"]

