from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# driver.implicitly_wait(10)
driver.get("https://abc.com/")
driver.maximize_window()
# sleep(3)
# var1 = driver.find_element(By.XPATH,"//a[@class='AnchorLink']/parent::li/desdendant::img)[1]")

wait_obj = WebDriverWait(driver, 10)

# loading = wait.until(EC.invisibility_of_element_located((By.ID,'preloader-animated_svg__circle')))
# title = driver.find_element(By.XPATH,)


