from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Property import Property

URL="https://docs.google.com/forms/d/e/1FAIpQLSevTljrBp9FLOSTULkWzliDCyXqLeQtI_XRmf565A0d_7x2ow/viewform?usp=header"

class GoogleForm:
    def __init__(self):
        super().__init__()
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

    def submit_form(self, property_item:Property):
        self.driver.get(URL)
        sleep(1)
        input_fields=self.driver.find_elements(By.CSS_SELECTOR, "form input[type='text']")
        address_field=input_fields[0]
        address_field.send_keys(property_item.address)
        rent_field=input_fields[1]
        rent_field.send_keys(property_item.price)
        bedroom_field=input_fields[2]
        bedroom_field.send_keys(property_item.bedrooms)
        bathroom_field=input_fields[3]
        bathroom_field.send_keys(property_item.bathrooms)
        sqft_field=input_fields[4]
        sqft_field.send_keys(property_item.sqft_living)
        agent_field=input_fields[5]
        agent_field.send_keys(property_item.agent)


        submit_btn=self.driver.find_element(By.XPATH, '//form/div[2]/div/div[3]/div/div/div')
        submit_btn.click()