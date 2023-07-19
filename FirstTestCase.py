import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=Service("C:\webdrivers\chromedriver.exe"))
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.back()
driver.maximize_window()
driver.implicitly_wait(5)
# dummy_ele = driver.find_elements(By.TAG_NAME, "a")
# print(dummy_ele)
print("-------------------->", driver.find_element(By.XPATH,"//h5[text()='Login']").is_displayed())
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print(driver.current_url)
# print(driver.page_source)


if driver.title == "OrangeHRM" :
    print("Test case was success")
    time.sleep(3)
else:
    print("Test case was failed")
    print(driver.title)
driver.close()







