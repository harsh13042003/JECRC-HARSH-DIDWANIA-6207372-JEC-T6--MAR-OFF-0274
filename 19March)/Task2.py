## select.is_multiple() --> if the options are multiple select or single select (True/False)
## select.deselect_by_index(index)
## select.deselect_all() --> deselects all option
## first_selected_option --> not a method/function; returns the first selected option; returns none
## all_selected_options --> not a method/function; returns list of options selected

## TASK 2: https://qavbox.github.io/demo/signup/


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

driver.get("https://qavbox.github.io/demo/signup/")
driver.maximize_window()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://qavbox.github.io/demo/signup/")
driver.maximize_window()

wait = WebDriverWait(driver, 20)

full_name = wait.until(EC.visibility_of_element_located((By.ID, "username")))
full_name.send_keys("Ajju")

# name = wait.until(EC.visibility_of_element_located((By.ID,'username')))

full_email = wait.until(EC.visibility_of_element_located((By.ID, "email")))
full_email.send_keys("azadsr15@gmail.com")

telephone = wait.until(EC.visibility_of_element_located((By.ID, "tel")))
telephone.send_keys("8597756496")

file = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@multiple='multiple']")))
if file.is_enabled():
    file.send_keys(r"C:\Users\azads\OneDrive\Pictures\wp4906270-4k-goku-pc-wallpapers.jpg")

gender = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@name='sgender']/option[2]")))
gender.click()

exp = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@name='experience'])[2]")))
exp.click()


skills = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='ip'])[2]")))
skills.click()

tools = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='tools']/option[2]")))
tools.click()

btn = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
btn.click()

# button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='submit'])[2]")))
