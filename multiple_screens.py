import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/windows")
driver.get("https://the-internet.herokuapp.com/nested_frames")

driver.maximize_window()
driver.implicitly_wait(3)
# driver.find_element(By.LINK_TEXT, "Click Here").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Elemental").click()
# parent_h = driver.current_window_handle
# handles = driver.window_handles
# titles = [driver.title]
# # for handle in handles:
# #     if handle != parent_h:
# #         driver.switch_to.window(handle)
# #         # time.sleep(6)
# #         titles.append(driver.title)
# # print(titles)
# # time.sleep(3)
#     # if title.startswith("New"):
#     #     time.sleep(3)
#     #     driver.switch_to.window()
#     # if title.startswith("Elemental"):
#     #     time.sleep(3)
#     #     driver.switch_to.window()
# for handle in handles:
#     driver.switch_to.window(handle)
#     if driver.title.startswith("The"):
#         print(driver.title)
#         time.sleep(1)
#     if driver.title.startswith("New"):
#         time.sleep(1)
#         print(driver.title)
#     if driver.title.startswith("Elemen"):
#         time.sleep(1)
#         print(driver.title)
# # driver.close()
driver.get("https://the-internet.herokuapp.com/nested_frames")
# driver.switch_to.frame(driver.find_element(By.XPATH, "//frame[@name='frame-top']"))
# print(driver.find_element(By.XPATH, "//frame[@name='frame-top']").get_attribute("src"))
top = driver.find_element(By.XPATH, "//frame[@name='frame-top']")
driver.switch_to.frame(top)
middle = driver.find_element(By.XPATH, "//frame[@name='frame-middle']")
left = driver.find_element(By.XPATH, "//frame[@name='frame-left']")
driver.switch_to.frame(middle)
print(driver.find_element(By.ID, "content").text)
driver.switch_to.parent_frame()
driver.switch_to.frame(left)
print(driver.find_element(By.TAG_NAME, "body").text)








