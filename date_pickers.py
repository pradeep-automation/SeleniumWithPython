import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=Service("C:\webdrivers\chromedriver.exe"))
driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
# driver.back()
# driver.forward()
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//span[@class='commonModal__close']").click()
time.sleep(2)
# driver.switch_to.frame()
driver.find_element(By.XPATH, "//p[@data-cy='departureDate']").click()

year = '2023'
month= 'October'
day = '5'
next_button_locator = "//div[@class='DayPicker-NavBar']/span[2]"
# previous_button_locator = (By.XPATH, "//div[@class='DayPicker-NavBar']/span[1]")
day_locator = f"//div[@class='dateInnerCell']/p[text()={day}]"

while True:
    current_month_year_element = driver.find_element(By.XPATH, "(//div[@class='DayPicker-Caption'])[1]")
    current_month_year = current_month_year_element.text
    driver.find_element(By.XPATH, next_button_locator).click()
    driver.find_element(By.XPATH, day_locator).click()
    time.sleep(3)




