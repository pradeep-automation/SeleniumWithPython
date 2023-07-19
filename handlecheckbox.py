import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
driver.find_element(By.ID,"name").send_keys("Pradeep")
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("8448921345")
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("noreply@testing.com")
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("noreply@testing.com")
driver.find_element(By.CSS_SELECTOR,"input[placeholder=Password]").send_keys("Random1234")
driver.find_element(By.TAG_NAME,"textarea").send_keys("123, test street, Uttarpradesh, 201009")
monday_checkbox=driver.find_element(By.CSS_SELECTOR,"input#monday")
monday_checkbox.click()
time.sleep(3)
# select all the checkboxs
days_checkbox = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
for days in days_checkbox:
    days.click()
print(monday_checkbox.is_selected())

time.sleep(7)
