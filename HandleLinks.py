import time

import requests
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.get("http://www.deadlinkcity.com/")
driver.get("https://www.moxtain.com/")
driver.maximize_window()
# click on link
# driver.find_element(By.LINK_TEXT,"Digital downloads").click()

# Find # on links in the page.
links = driver.find_elements(By.TAG_NAME, 'a')
total_links = len(links)
print(total_links)

# for i, link in enumerate(links):
#     print(f'{i}----->{link.text}')
count = 0
for link in links:
    link_url = link.get_attribute("href")
    try:
        res = requests.head(link_url)
        if res.status_code >= 400:
            print(f'{link_url} --------- is a broken link')
            count += 1
        else:
            print(f'{link_url} ------ is a valid link')
    except requests.RequestException as e:
        print(f"Error for link url {link_url}: {e}")


print(f'total number of broken links are {count}')

time.sleep(2)
driver.close()
