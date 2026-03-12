from selenium import webdriver
import time

browsers = [webdriver.Chrome, webdriver.Firefox, webdriver.Edge]

for browser in browsers:
    driver = browser()

    driver.maximize_window()
    driver.get("https://google.com")

    print("Browser:", browser.__name__)
    print("Title:", driver.title)
    print("Current URL:", driver.current_url)
    print("----------------------")

    time.sleep(3)
