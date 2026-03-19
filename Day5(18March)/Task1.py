from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/')
sleep(3)

cblink = driver.find_element(By.LINK_TEXT, "Checkboxes")
print('cblink found')

ddlink = driver.find_element(By.PARTIAL_LINK_TEXT, "Drag and Drop")
print('ddlink found')

listdata = driver.find_elements(By.TAG_NAME, "li")
print('total li:', len(list_data))

driver.get('https://the-internet.herokuapp.com/tables')
sleep(3)

val1 = driver.find_element(By.XPATH, "//table[@id='table1']//td[text()='jdoe@hotmail.com']/following-sibling::td[2]")
print('val1 found')

val2 = driver.find_element(By.XPATH,"//table[@id='table1']//td[text()='Bach']/following-sibling::td[5]/a[2]")
print('val2 found')

t2 = driver.find_element(By.XPATH, "//table[2]")
print('t2 found')

parent_found = driver.find_element(By.XPATH,"//table[@id='table2']//td[text()='$100.00']/parent::tr")
print('parent_found found')
driver.quit()