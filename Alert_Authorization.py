import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

# wait =  WebDriverWait(driver, 10)
# alert_box = wait.until(expected_conditions.alert_is_present(),"Not available")
# user = "admin"
# password = "admin"
# alert_box.send_keys(f'{user}\n{password}')
# alert_box.accept()
time.sleep(3)