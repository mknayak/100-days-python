from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class InternetSpeedTwitterBot:
    def __init__(self):
        super().__init__()
        self.down=0
        self.up=0
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome()


    def get_internet_speed(self):
        url="https://www.speedtest.net"
        self.driver.get(url)
        go_button= self.driver.find_element(By.CLASS_NAME, "js-start-test")
        go_button.click()
        sleep(60)
        self.down=float(self.driver.find_element(By.CSS_SELECTOR, ".result-data-value.download-speed").text)
        self.up=float(self.driver.find_element(By.CSS_SELECTOR, ".result-data-value.upload-speed").text)
        self.driver.quit()

    def tweet_at_provider(self):
        pass