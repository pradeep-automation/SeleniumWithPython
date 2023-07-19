import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Digital downloads").click()
time.sleep(2)
driver.close()