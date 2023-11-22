import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.get("https://www.google.com")
driver.maximize_window()
wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=())
search_box = wait.until(
    expected_conditions.visibility_of_element_located((By.NAME, "q")))

search_box.send_keys("Selenium", Keys.ENTER)

text_to_select = "selenium interview questions"

ul_search = driver.find_element(By.XPATH, "(//ul[@role='listbox'])[1]")
time.sleep(3)
# print(ul_search)
li_box = ul_search.find_elements(By.XPATH, "//li")
# print(li_box)
for item in li_box:
    print(item.text)
for item in li_box:

    if text_to_select in item.get_attribute("innerText"):
        item.click()
        break

time.sleep(5)
