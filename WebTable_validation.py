# Webtable can be of two types
# Dynamic table and Static table

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Count number of rows and columns

rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
columns = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/th")
print(f'There are total {len(rows)} rows and {len(columns)} column in the BookTable')

# Read specific row and column data

for row in range(2,len(rows)+1):
    for col in range(1,len(columns)+1):
        value = driver.find_element(By.XPATH,f"//table[@name='BookTable']//tr[{row}]/td[{col}]").text
        print(f'value at tr[{row}],td[{col}] is {value}')


