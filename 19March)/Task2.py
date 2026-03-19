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
