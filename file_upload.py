import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller

driver = webdriver.Chrome()
driver.get("https://imgbb.com/")
driver.maximize_window()

upload_nav= driver.find_element(By.CSS_SELECTOR, "li[data-nav='upload']")
upload_nav.click()
time.sleep(5)
upload_link = driver.find_element(By.XPATH, "//a[contains(text(),'browse')]")
upload_link.click()
time.sleep(2)

# upload_file_input = driver.find_element(By.CSS_SELECTOR, "#anywhere-upload-input")
file_path = "C:\\Users\\pradeep.ramola\\Downloads\\selenium_up.PNG"

keyboard = Controller()
keyboard.type(file_path)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(5)

handles = driver.window_handles




