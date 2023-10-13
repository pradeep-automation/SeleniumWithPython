import time

import requests
from selenium import webdriver

# Create a new instance of the browser driver (e.g., Firefox, Chrome)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://the-internet.herokuapp.com/broken_images")

# Find all image elements on the page
image_elements = WebDriverWait(driver, 10).until(
    expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, ".example img")))
# print(image_elements)

# Loop through each image element and check for errors
for image in image_elements:
    src = image.get_attribute("src")
    print(src)
    # response = driver.execute_script(
    #     "return arguments[0].complete && typeof arguments[0].naturalWidth !== 'undefined'", image
    # )
    # print(response)
    response = requests.get(src)

    if response.status_code != 200:
        print(f"Broken image found: {src}")


# Close the browser
driver.quit()
