from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()

# 1. open website
driver.get("https://www.amazon.in/")
sleep(4)

print("Amazon website opened")

# 2. locate search bar using CSS selector (ID)
search_bar = driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox")
print("Search bar located")
print(search_bar)

# 3. locate Amazon logo using CSS selector
logo = driver.find_element(By.CSS_SELECTOR,"#nav-logo-sprites")
print("Amazon logo located")
print(logo)

# 4. locate Cart link/icon
cart = driver.find_element(By.CSS_SELECTOR,"#nav-cart")
print("Cart icon located")
print(cart)

# 5. locate Sign in link using descendant selector
signin = driver.find_element(By.CSS_SELECTOR,"#nav-tools #nav-link-accountList")
print("Sign in section located")
print(signin)

# 6. locate all category links under navigation bar
categories = driver.find_elements(By.CSS_SELECTOR,"#nav-xshop a")
print("Number of category links:", len(categories))
print(categories)

sleep(3)

driver.quit()
