from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://google.com")

print("Browser: Chrome")
print("Title:", driver.title)
print("Current URL:", driver.current_url)

time.sleep(2)

driver.refresh()
driver.back()
driver.forward()

time.sleep(2)

driver.quit()