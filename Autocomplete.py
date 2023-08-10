import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
search_box = WebDriverWait(driver, 10, ignored_exceptions=()).until(
    expected_conditions.visibility_of_element_located((By.NAME, "q")))

search_box.send_keys("Selenium")

text_to_select = "selenium webdriver"

ul_search = driver.find_element(By.XPATH, "//ul[@role='listbox']")
li_box = ul_search.find_elements(By.TAG_NAME, "li")
print(li_box)
for item in li_box:
    if text_to_select in item.get_attribute("innerText"):
        item.click()
        break

time.sleep(2)


import tempfile

print(tempfile)
