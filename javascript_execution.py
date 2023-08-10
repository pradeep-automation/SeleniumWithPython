import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class JavaScriptExecution:

    def test(self):
        driver = webdriver.Chrome()
        driver.execute_script("window.location = 'https://www.google.com'")
        driver.maximize_window()
        driver.execute_script("return document.querySelector('textarea[name=\"q\"]')").send_keys("selenium", Keys.ENTER)
        time.sleep(2)
        height = driver.execute_script("return window.innerHeight")
        width = driver.execute_script("return window.innerWidth")
        # print(height, width)
        driver.execute_script("window.scroll(400, 100)")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, 1000)")
        time.sleep(2)
        driver.execute_script("window.scroll(0, 0)")
        time.sleep(2)
        # Scroll element into view
        element = driver.find_element(By.ID, "x")
        location = element.location_once_scrolled_into_view
        # Returns the element into view as well as the location
        # of the element in the page from top left of the corner.
        # javacript way
        driver.execute_script("arguments[0].scrollIntoView(true)", element)




ff = JavaScriptExecution()
ff.test()


