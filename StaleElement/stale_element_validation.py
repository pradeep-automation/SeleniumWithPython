import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("C:\\Development\\robot-scripts\\SeleniumWithPython\\StaleElement\\stale_element_page.html")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
element = driver.find_element(By.XPATH,"//a[text()='Item 1']")
button = driver.find_element(By.XPATH,"//button")
button.click()
wait.until(EC.staleness_of(element))




_locator = "//a[text()='Updated Item 1']"

print("Element is visible----->",driver.find_element(By.XPATH, _locator).is_displayed())
time.sleep(3)


ele = wait.until(EC.presence_of_all_elements_located((By.ID, "name")))


