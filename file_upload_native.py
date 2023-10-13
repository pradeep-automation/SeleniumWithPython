import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
# driver.get("https://www.plupload.com/examples/")
driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()

file_path = "C:/Users/pradeep.ramola/Documents/house_rent/apr_jun_rent.JPG"
upload_file = driver.find_element(By.CSS_SELECTOR, "input[type='File']")
upload_file.send_keys(file_path)
# try:
#     driver.execute_script("arguments[0].value = arguments[1];", file_path)
#     print("Uploaded successfully")
# except:
#     print("Failed!!!!!!")

time.sleep(4)