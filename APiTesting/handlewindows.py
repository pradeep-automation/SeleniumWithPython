import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Windows.html")
# driver.find_element(By.CSS_SELECTOR, "div .pullleft>ul li:nth-child(1)").click()
driver.find_element(By.XPATH, "//div[@id='Tabbed']/a/button").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "div .pullleft>ul li:nth-child(3)").click()

driver.find_element(By.XPATH, "//div[@id='Multiple']/button").click()
time.sleep(3)
parent_handle = driver.current_window_handle
# print(parent_handle)
handles = driver.window_handles
title_parent = "Frames & windows"
sec_title = "Selenium"
titles_to_keep = [title_parent, sec_title]
third_title = "Index"
for handle in handles:
    driver.switch_to.window(handle)
    if driver.title not in titles_to_keep:
        driver.close()
        time.sleep(5)

print(driver.title)

