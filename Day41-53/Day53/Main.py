from Day53.GoogleForm import GoogleForm
from PropertyGuru import *

pg=PropertyGuru()
properties = pg.get_property_listing(1)

form= GoogleForm()
for prop in properties:
    form.submit_form(prop)
    sleep(1)