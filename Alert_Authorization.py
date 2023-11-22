import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://uk.sagepub.com/en-gb/eur/home")
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
# time.sleep(3)

driver.find_element(By.CSS_SELECTOR, ".modal-header button.modal-close").click()
# driver.find_element(By.XPATH, '//ul[contains(@class, "navbar-nav")]//a[@id="menu-item-31229"]').click()
# driver.find_element(By.XPATH, "//ul[@name='navigation-item-31229']//a[text()= 'Books']").click()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR, ".modal-header button.modal-close").click()
driver.find_element(By.ID, "edit-keys-33").send_keys("Psychology")
results = driver.find_element(By.XPATH, '//div[@class="tt-dataset-search-filters"]')
# print(results.get_attribute("innerHTML"))
#
result_list = results.find_elements(By.XPATH, "//span/div/p")
for result in result_list:
    if result.text == "Psychology in Journals":
        result.click()
        break
time.sleep(3)

