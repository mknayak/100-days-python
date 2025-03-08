from datetime import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

URL="https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"


driver.get(URL)
sleep(3)
google_link = driver.find_element(By.XPATH,'//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[1]/div/div//iframe')
google_link.click()

base_window = driver.window_handles[0]
sign_in_window = driver.window_handles[1]

driver.switch_to.window(sign_in_window)
sleep(3)
print(driver.title)
email_field= driver.find_element(By.NAME, 'identifier')
email_field.send_keys('study.creekworm@gmail.com')
button_sign_in = driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button')
sleep(3)
button_sign_in.click()



#driver.quit()