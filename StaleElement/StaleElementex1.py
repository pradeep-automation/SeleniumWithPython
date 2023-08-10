import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

# Initialize the WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

try:
    # Open Google homepage
    driver.get("https://www.google.com")

    # Locate the search input element
    search_input = driver.find_element(By.NAME, "q")

    # Enter a search term and submit
    search_input.send_keys("Selenium WebDriver")
    search_input.submit()

    # Locate the search results
    search_results = WebDriverWait(driver, 10)\
        .until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, "h3")))
    # search_results = driver.find_elements(By.CSS_SELECTOR, "h3")


    # Print the search results titles
    for result in search_results:
        try:
            print(result.text)

        except StaleElementReferenceException:
            # Handle StaleElementReferenceException
            print("StaleElementReferenceException occurred. Retrying...")

except Exception as e:
    print("An error occurred:", str(e))
# #
# finally:
#     # Close the browser
#     driver.quit()
