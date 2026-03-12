from selenium import webdriver
import time

# -------- Chrome Browser --------
print("Opening Chrome Browser")

chrome_opts = webdriver.ChromeOptions()
chrome_opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_opts)
driver.maximize_window()
driver.get("https://supertails.com/")

print("Title:", driver.title)
print("Current URL:", driver.current_url)

time.sleep(2)

driver.refresh()
driver.back()
driver.forward()




# -------- Firefox Browser --------
print("Opening Firefox Browser")

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://supertails.com/")

print("Title:", driver.title)
print("Current URL:", driver.current_url)

time.sleep(2)

driver.refresh()
driver.back()
driver.forward()




# -------- Edge Browser --------
print("Opening Edge Browser")

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://supertails.com/")

print("Title:", driver.title)
print("Current URL:", driver.current_url)

time.sleep(2)

driver.refresh()
driver.back()
driver.forward()