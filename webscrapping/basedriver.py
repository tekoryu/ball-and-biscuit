from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.options import Options

class BaseDriver:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--disable-extensions")
        #self.options.headless = True
        self.driver = webdriver.Chrome(service=Service(self.options))

    def get_driver(self):
        return self.driver
    def quit(self):
        self.driver.quit()