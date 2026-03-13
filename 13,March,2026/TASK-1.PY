from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.cricbuzz.com")
sleep(5)


css1 = driver.find_element(By.CSS_SELECTOR,"a[title='Live Cricket Score']")
print("CSS1 :", css1.text)

css2 = driver.find_element(By.CSS_SELECTOR,"a[title='Cricket Schedule']")
print("CSS2 :", css2.text)

css3 = driver.find_element(By.CSS_SELECTOR,"a[title='Cricket Series']")
print("CSS3 :", css3.text)

print("CSS selectors working")



x1 = driver.find_element(By.XPATH,"//a[@title='Live Cricket Score']")
print("XPath1 :", x1.text)

x2 = driver.find_element(By.XPATH,"//a[@title='Cricket Schedule']")
print("XPath2 :", x2.text)

x3 = driver.find_element(By.XPATH,"//a[@title='Cricket Series']")
print("XPath3 :", x3.text)

print("XPath attribute working")



t1 = driver.find_element(By.XPATH,"//a[text()='Series']")
print("Text1 :", t1.text)

t2 = driver.find_element(By.XPATH,"//a[text()='Teams']")
print("Text2 :", t2.text)

t3 = driver.find_element(By.XPATH,"//a[text()='News']")
print("Text3 :", t3.text)

print("XPath inner text working")


sleep(3)
driver.quit()


sleep(3)

driver.quit()
