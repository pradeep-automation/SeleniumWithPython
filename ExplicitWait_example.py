from selenium import webdriver
from selenium.common import StaleElementReferenceException, TimeoutException, NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.maximize_window()
wait = WebDriverWait(driver, 5, poll_frequency=2, ignored_exceptions=[])
driver.find_element(By.XPATH, "//button").click()

try:
    element = wait.until(EC.visibility_of_element_located((By.ID,"finish")))
    print(f"{element.text} Element shown up")
except StaleElementReferenceException:
    print("Element not visible")
