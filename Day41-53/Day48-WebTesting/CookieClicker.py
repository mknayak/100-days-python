import random
from datetime import timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver= webdriver.Chrome(options=options)
URL="http://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)

cookie = driver.find_element(By.ID, "cookie")

start_time= time.time()
play_time= time.time() + (60*5)

continue_game=True


def random_active_tag():
    buy_options = driver.find_elements(By.CSS_SELECTOR, "#store div")
    active_options = []
    for option in buy_options:
        if option.get_attribute("class") != "grayed":
            active_options.append({
                "tag": option,
                "amount": int(re.findall(r'\d+', option.text)[0])})
    if len(active_options) == 0:
        return None

    return random.choice(active_options)["tag"]



while continue_game:
    cookie.click()
    if time.time() > play_time:
        continue_game=False
    if time.time() > start_time+5:
        start_time=time.time()
        money= int(re.findall(r'\d+', driver.find_element(By.ID, "money").text)[0])
        active_tag=random_active_tag()
        active_tag.click()


