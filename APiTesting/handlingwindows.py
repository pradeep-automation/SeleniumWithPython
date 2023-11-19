
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/")
parent_handle = driver.current_window_handle
usr = driver.find_element(By.NAME, "username")
usr.send_keys("Admin")
pwd= driver.find_element(By.NAME, "password")
pwd.send_keys("admin123")
log_btn = driver.find_element(By.TAG_NAME, "button")
log_btn.click()

driver.find_element(By.XPATH, '//a[@href="http://www.orangehrm.com"]').click()

handles = driver.window_handles

for handle in handles:
    if handle != parent_handle:
        driver.switch_to.window(handle)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(4)
        driver.find_element(By.XPATH, '//a[contains(text(),"Open Source HRMS")]').click()

time.sleep(3)

for handle in driver.window_handles:

    driver.switch_to.window(handle)
    # print(driver.current_url)
    if "Free" not in driver.title:
        driver.close()

    else:
        print(driver.title)
        time.sleep(5)







titles = ["OrangeHRM", "OrangeHRM HR Software | OrangeHRM"]

