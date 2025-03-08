from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from Property import *

URL="https://www.propertyguru.com.sg/property-for-rent"
FILTERS="bedrooms=0&bedrooms=1&bedrooms=2&bedrooms=3&bedrooms=4&bedrooms=5&minPrice=2500&maxPrice=3500&propertyTypeGroup=H&propertyTypeCode=1R&propertyTypeCode=2A&propertyTypeCode=2I&propertyTypeCode=2S&propertyTypeCode=2RF&propertyTypeCode=3A&propertyTypeCode=3NG&propertyTypeCode=3Am&propertyTypeCode=3NGm&propertyTypeCode=3I&propertyTypeCode=3Im&propertyTypeCode=3S&propertyTypeCode=3STD&propertyTypeCode=3PA&propertyTypeCode=4A&propertyTypeCode=4NG&propertyTypeCode=4PA&propertyTypeCode=4I&propertyTypeCode=4S&propertyTypeCode=4STD&propertyTypeCode=5A&propertyTypeCode=5PA&propertyTypeCode=5I&propertyTypeCode=5S&propertyTypeCode=6J&propertyTypeCode=EA&propertyTypeCode=EM&propertyTypeCode=MG&propertyTypeCode=TE&isCommercial=false"

class PropertyGuru:
    def __init__(self):
        super().__init__()
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver= webdriver.Chrome(options=options)
        self.url=URL
        self.filters=FILTERS

    def get_property_listing(self,page)->list[Property]:
        final_url=f"{self.url}/{page}?{self.filters}"
        self.driver.get(final_url)
        sleep(2)
        properties=[]
        property_nodes= self.driver.find_elements(By.CSS_SELECTOR, ".search-result-root .listing-card-banner-root")
        for property_node in property_nodes:
            address= property_node.find_element(By.CSS_SELECTOR, "div.detail-group h3.listing-title").text
            list_fields=property_node.find_elements(By.CSS_SELECTOR,"div.detail-group li.info-item")
            bedrooms=list_fields[0].text
            baths=list_fields[1].text
            sqft=list_fields[2].text
            price=property_node.find_element(By.CSS_SELECTOR,"div.detail-group div.listing-price").text
            agent= property_node.find_element(By.CSS_SELECTOR,"div.agent-name-rating").text
            properties.append(Property(address,bedrooms,baths,price,agent,sqft))

        return properties