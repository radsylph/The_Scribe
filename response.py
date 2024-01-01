from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")


class Selenium:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.google.com")

    def testSelenium(self):
        print("Selenium ran")
        self.driver.close()

    def giveDolar(self) -> str:
        driver = self.driver
        driver.get("https://www.bcv.org.ve")
        dolarPrice = driver.find_element(By.ID, "dolar")
        print(dolarPrice.text)
        return dolarPrice.text

    def brickSeekTest1(self, upc_code: str) -> str:
        driver = self.driver
        driver.get("https://brickseek.com/walmart-inventory-checker")
        
