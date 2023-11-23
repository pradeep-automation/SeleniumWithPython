# Mouse Hover
# Double click
# Right Click
# Drag and Drop
# Drag and Drop by offset
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# xpaths for the users dropdown
_admin_tab = "//ul[@class='oxd-main-menu']/li[1]"
_user_mgt = "//nav[@aria-label='Topbar Menu']//li[1]"
_users = "//a[text()='Users']"


action = ActionChains(driver)
time.sleep(3)
# Mouse hover action
action.move_to_element(driver.find_element(By.XPATH, _admin_tab)).click().perform()
driver.find_element(By.XPATH, _user_mgt).click()
action.move_to_element(driver.find_element(By.XPATH, _users)).click().perform()
# action.context_click(<element>(default is None and will be simple right click))
action.context_click().perform()
time.sleep(5)
from pynput.keyboard import Controller, Key
keyb = Controller()
keyb.press(Key.down)
keyb.release(Key.down)

# right click using context_click()
# action.context_click(driver.find_element(By.XPATH, _user_mgt)).perform()

# Scroll page down using pixels
# driver.execute_script("window.scrollBy(0, 3000)")
# time.sleep(3)
# loc = driver.execute_script("return window.pageYOffset")
# print(loc)



# Scroll down page until the end of the page

driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")







