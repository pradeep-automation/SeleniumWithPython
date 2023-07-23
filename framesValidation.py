import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame(0)


driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
time.sleep(3)
driver.switch_to.default_content()
driver.switch_to.frame(1)
driver.find_element(By.XPATH, "//span[text()='WebDriver']").click()
driver.switch_to.default_content()
driver.switch_to.frame("classFrame")

driver.find_element(By.XPATH, "//div[@class='topNav']//a[text()='Help']").click()
time.sleep(10)