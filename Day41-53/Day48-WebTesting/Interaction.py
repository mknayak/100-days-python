from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

URL="https://en.wikipedia.org/wiki/Main_Page"



options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get(URL)
article_count =driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a')
print(article_count.text)
article_count.click()

input_box= driver.find_element(By.NAME, 'search')
input_box.send_keys('python')
input_box.send_keys(Keys.ENTER)




#driver.quit()