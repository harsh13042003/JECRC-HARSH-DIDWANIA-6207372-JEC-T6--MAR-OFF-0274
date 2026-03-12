from selenium import webdriver
import time

browsers = [webdriver.Chrome, webdriver.Firefox, webdriver.Edge]

for browser in browsers:
    driver = browser()

    driver.maximize_window()
    driver.get("https://google.com")

    print("Browser:", browser.__name__)
    time.sleep(3)


