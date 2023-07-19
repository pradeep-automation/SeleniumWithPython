from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
log_btn = driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'login-button')]")
print("value of attribute is--------------->", log_btn.get_attribute('value'))
print(log_btn.text)

