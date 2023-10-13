import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/dropdown")
# driver.maximize_window()
element = driver.find_element(By.ID, "dropdown")
select_drop = Select(element)

# select_drop.select_by_value("1")
# select_drop.select_by_visible_text("Option 2")
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
from_ele = driver.find_element(By.XPATH, "//div[@id='column-a']")
to_ele = driver.find_element(By.XPATH, "//div[@id='column-b']")
to_ele_final = driver.find_element(By.CSS_SELECTOR, "#column-b header")
actions = ActionChains(driver)
actions.drag_and_drop(to_ele, from_ele).perform()
# actions.click_and_hold(to_ele).move_to_element(from_ele).release(from_ele).perform()

print(to_ele_final.text)
assert to_ele_final.text == 'A'


driver.back()
time.sleep(1)
