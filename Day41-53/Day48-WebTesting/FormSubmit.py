from selenium import webdriver
from selenium.webdriver.common.by import By

URL="http://secure-retreat-92358.herokuapp.com"
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver= webdriver.Chrome(options=options)
driver.get(URL)

fName=driver.find_element(By.NAME,"fName")
fName.clear()
fName.send_keys("Manas")
lName=driver.find_element(By.NAME,"lName")
lName.clear()
lName.send_keys("Test")
email=driver.find_element(By.NAME,"email")
email.clear()
email.send_keys("manas@testemail.com")

button=driver.find_element(By.CSS_SELECTOR,"form button")
button.click()

driver.quit()