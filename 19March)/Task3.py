from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")

wait = WebDriverWait(driver, 25)
search = wait.until(EC.element_to_be_clickable((By.ID, "twotabsearchtextbox")))
search.send_keys("bmw m5 cs")
suggestion_xpath = "//div[@class='left-pane-results-container']//div[@role='button']"
wait.until(EC.presence_of_all_elements_located((By.XPATH, suggestion_xpath)))

suggestions = driver.find_elements(By.XPATH, suggestion_xpath)
if len(suggestions) >= 4:
    suggestions[3].click()

sort_btn = wait.until(EC.element_to_be_clickable((By.ID, "a-autoid-0-announce")))
sort_btn.click()

newest = wait.until(EC.element_to_be_clickable((By.ID, "s-result-sort-select_4")))
newest.click()

free_xpath = "//span[contains(text(),'Free Shipping') or contains(text(),'All items')]/preceding-sibling::div//input"
checkbox = wait.until(EC.presence_of_element_located((By.XPATH, free_xpath)))

driver.execute_script("arguments[0].click();", checkbox)

wait.until(EC.presence_of_element_located((By.XPATH, "(//h2//span)[1]")))

name = driver.find_element(By.XPATH, "(//h2//span)[1]").get_attribute("textContent")
price = driver.find_element(By.XPATH, "(//span[@class='a-price-whole'])[1]").get_attribute("textContent")


print("Product:", name.strip())
print("Price: ", price.strip())

driver.quit()

