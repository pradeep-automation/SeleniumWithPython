import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller

def file_upload_func(file: str):
    keyboard = Controller()
    keyboard.type(file)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

driver = webdriver.Chrome()
driver.get("https://imgbb.com/")
driver.maximize_window()

upload_nav= driver.find_element(By.CSS_SELECTOR, "li[data-nav='upload']")
upload_nav.click()
time.sleep(2)
upload_link = driver.find_element(By.XPATH, "//a[contains(text(),'browse')]")
upload_link.click()
time.sleep(2)

file_path = "C:\\Users\\pradeep.ramola\\Downloads\\Resignation_gl.jpg"
# upload_file_input = driver.find_element(By.CSS_SELECTOR, "#anywhere-upload-input")
# upload_file_input.send_keys(file_path)

file_upload_func(file_path)
time.sleep(5)



