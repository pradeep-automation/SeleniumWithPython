from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.flipkart.com/")
log_cross = driver.find_element(By.CLASS_NAME, "_30XB9F")
log_cross.click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.invisibility_of_element(log_cross))
driver.find_element(By.CLASS_NAME, "Pke_EE").send_keys("kinder")
time.sleep(3)
ul_pro = driver.find_elements(By.XPATH, "//ul[contains(@class, '_2x2Mmc')]/li")
ls = []
for i in ul_pro:
    ls.append(i.text)

time.sleep(3)
print(ls)
# main_div = driver.find_elements(By.CSS_SELECTOR, ".left-pane-results-container div .s-suggestion-container")
# ls = []
# for divs in main_div:
#     ls.append(divs.text)
# print(ls)



# driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_ajax_first")
# driver.switch_to.frame("iframeResult")
#
# wait = WebDriverWait(driver, 4)
# try:
#     element = wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//h2[text()='AJAX']")))
#
# except TimeoutException as ne:
#     driver.find_element(By.XPATH,"//button[@type='button']").click()
#     print(driver.find_element(By.XPATH, "//h1[text()='AJAX']").text)

action = ActionChains(driver)
action.drag_and_drop( r)


