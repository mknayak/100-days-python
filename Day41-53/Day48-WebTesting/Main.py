from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

events_list = driver.find_elements(By.CSS_SELECTOR, 'div.event-widget ul li')

events= {}
index=0
for event in events_list:
    events[index]={
        'date': event.find_element(By.TAG_NAME,'time').text,
        'topic': event.find_element(By.TAG_NAME,'a').text
    }
    index+=1

print(events)
#driver.close()  #Close tab
driver.quit() #CLose Browser