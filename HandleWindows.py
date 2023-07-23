import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=Service("C:\webdrivers\chromedriver.exe"))
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
# window_id = driver.current_window_handle
# print(window_id)
time.sleep(4)
driver.find_element(By.XPATH,"//p//a").click()
# next_window.click()
time.sleep(5)
window_ids = driver.window_handles
for window_id in window_ids:
    if window_id is not driver.current_window_handle:
        driver.switch_to.window(window_id)
        print(driver.title)
        # driver.find_element(By.XPATH,"//div[contains(@class,'web-menu-btn')]//button[text()='Book a Free Demo']").click()
        # if driver.find_element(By.XPATH
        #                        , "//div[@class='free-demo-page-description']//h4").text == "See the endless possibilities with OrangeHRM.":
        #     print("It was successful")


