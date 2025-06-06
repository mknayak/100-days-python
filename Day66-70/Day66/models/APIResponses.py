class CafeResponse:
    def __init__(self,id:int):
       self.id=id
       self.can_take_calls=False
       self.coffee_price=0
       self.has_sockets=True
       self.has_toilet=True
       self.img_url="htp://google.com"
       self.location="Singapore"
       self.map_url="maps.google.com/s/singapore"
       self.name="Kitty Cafe"
       self.seats=20

    def serializable(self):
       return {}