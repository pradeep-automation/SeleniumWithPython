import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# driver.implicitly_wait(10)    # will be applied all the elements in the web page and wait for max 10 seconds.
my_wait = WebDriverWait(driver, 10, poll_frequency=3, ignored_exceptions=[NoSuchElementException,
                                                                          ElementNotVisibleException,
                                                                          ElementNotInteractableException])  # Explicit wait declaration
driver.get("https://www.google.com/")
driver.maximize_window()
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys('Selenium')
search_box.submit()
# time.sleep(3)
selenium_off = my_wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text() = 'Selenium']")))
# selenium_off = driver.find_element(By.XPATH, "//h3[text() = 'Selenium']")
selenium_off.click()
time.sleep(3)
