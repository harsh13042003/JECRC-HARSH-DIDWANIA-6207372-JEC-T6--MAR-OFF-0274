from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")
sleep(3)

print("Website opened successfully")

# Username field
username = driver.find_element(By.XPATH,"//input[@name='username']")
print("Username field located, tag:", username.tag_name)

# Password field
password = driver.find_element(By.XPATH,"//input[@id='password']")
print("Password field located, tag:", password.tag_name)

# Login button
login_btn = driver.find_element(By.XPATH,"//button[@type='submit']")
print("Login button text:", login_btn.text)

# Elemental Selenium link
link = driver.find_element(By.XPATH,"//a[text()='Elemental Selenium']")
print("Link text:", link.text)

# Heading
heading = driver.find_element(By.XPATH,"//h2[contains(text(),'Login Page')]")
print("Heading:", heading.text)

sleep(3)

print("All elements located successfully")

driver.quit()