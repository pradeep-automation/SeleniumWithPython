import time

from selenium import webdriver

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=ops)
driver.get("https://whatmylocation.com/")
driver.maximize_window()
time.sleep(10)
