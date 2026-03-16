from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()


driver.get("https://demoqa.com/radio-button")
sleep(3)


print("Page Title:", driver.title)


yes_radio = driver.find_element(By.ID,"yesRadio")


driver.execute_script("arguments[0].click();", yes_radio)
print("Yes radio button clicked")

sleep(2)


result = driver.find_element(By.CLASS_NAME,"text-success")
print("Result message:", result.text)


print("Class attribute:", yes_radio.get_attribute("class"))
print("ID attribute:", yes_radio.get_attribute("id"))


print("Current URL:", driver.current_url)

sleep(3)
driver.quit()