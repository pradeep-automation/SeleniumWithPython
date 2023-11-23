from selenium import webdriver
from selenium.common import StaleElementReferenceException, TimeoutException, NoSuchElementException, \
    ElementNotVisibleException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.maximize_window()
wait = WebDriverWait(driver, 15, poll_frequency=2, ignored_exceptions=(TimeoutException,))
# driver.find_element(By.XPATH, "//button").click()

try:
    start_btn = driver.find_element(By.TAG_NAME, "button")
    # driver.execute_script("arguments[0].scrollIntoView();", start_btn)
    start_btn.click()
    # start_btn = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
    # start_btn.click()
    element = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    # element.send_keys("xxx")

    print(f"{element.text} Element shown up")

except StaleElementReferenceException:
    print("Element not visible")
except ElementNotInteractableException as ei:
    print(ei)


