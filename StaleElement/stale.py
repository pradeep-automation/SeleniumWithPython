import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

url = "file:///C://Development//robot-scripts//SeleniumWithPython//StaleElement//stale_element_page.html"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

before = driver.find_element(By.XPATH, "//a[text()='Item 1']")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(3)
wait = WebDriverWait(driver, 10)
ele = wait.until(expected_conditions.staleness_of(before))
if ele:
    print("not available anymore")

