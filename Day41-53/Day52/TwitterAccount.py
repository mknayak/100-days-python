from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TwitterAccount:
    def __init__(self):
        super().__init__()
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        self.login_url="https://www.instagram.com"

    def login(self, username, password):
        self.driver.get(self.login_url)
        sleep(3)
        username_field=self.driver.find_element(By.NAME, "username")
        password_field=self.driver.find_element(By.NAME, "password")
        login_button=self.driver.find_element(By.TAG_NAME, "button")
        username_field.send_keys(username)
        sleep(1)
        password_field.send_keys(password)
        sleep(1)
        login_button.click()
        sleep(10)

    def find_user(self,username):
        self.driver.get(f"{self.login_url}/{username}")
        sleep(5)
        follower_link=self.driver.find_element(By.XPATH, '//main/div/header/section[3]/ul/li[2]')
        follower_link.click()
        sleep(5)
        popup_1= self.driver.find_element(By.ID,'scrollview')
        buttons = popup_1.parent.find_elements(By.TAG_NAME, 'button')
        follow_buttons = [n for n in buttons if n.text == 'Follow']
        sleep(1)
        for follow_button in follow_buttons:
            try:
                follow_button.click()
                sleep(1)
            except:
                pass



    def logout(self):
        self.driver.quit()