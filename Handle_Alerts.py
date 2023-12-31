import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
loc_alert_box_name = "alert"
loc_alert_box_confirm = "confirmation"
loc_alert_box_prompt = "prompt"
driver.find_element(By.NAME, loc_alert_box_name).click()

# driver.find_element(By.NAME, loc_alert_box_name).click()
# alert_box = Alert(driver)
# print(alert_box.text)

time.sleep(2)
alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.accept()

driver.find_element(By.NAME, loc_alert_box_confirm).click()
alert_confirm = driver.switch_to.alert
print(alert_confirm.text)
time.sleep(2)
alert_confirm.dismiss()

driver.find_element(By.NAME, loc_alert_box_prompt).click()
alert_prompt = driver.switch_to.alert
print(alert_prompt.text)
from pynput.keyboard import Controller, Key
keyb = Controller()
keyb.type("I am Pradeep")
# alert_prompt.send_keys("I am Pradeep")
time.sleep(7)
alert_prompt.accept()
driver.quit()
