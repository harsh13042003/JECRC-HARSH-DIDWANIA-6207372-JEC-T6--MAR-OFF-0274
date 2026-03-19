from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
sleep(3)
print("Page Title:", driver.title)
username = driver.find_element(By.NAME, "username")
username.clear()
username.send_keys("Admin")
password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")
login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
login_btn.click()
sleep(4)
current_url = driver.current_url
print("Current URL:", current_url)
if "dashboard" in current_url.lower():
    print("Successful login")
sleep(3)
