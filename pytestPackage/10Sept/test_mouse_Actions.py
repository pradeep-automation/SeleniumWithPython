import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class TestMagento:
    women_drpdown_locator = "//span[text()='Women']"
    women_tops_locator = "(//span[text()='Tops'])[1]"
    women_jackets_locator = "(//span[text()='Jackets'])[1]"
    search_box_loc = "search"

    @pytest.fixture
    def set_up(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://magento.softwaretestingboard.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    def test_search_results(self, set_up):
        print(self.driver.title)
        women_drpdown = self.driver.find_element(By.XPATH,self.women_drpdown_locator)
        action = ActionChains(self.driver)
        time.sleep(5)
        action.move_to_element(women_drpdown).perform()

        women_tops = self.driver.find_element(By.XPATH,self.women_tops_locator)
        action.move_to_element(women_tops).perform()
        women_jackets = self.driver.find_element(By.XPATH,self.women_jackets_locator)
        action.move_to_element(women_jackets).perform()
        women_jackets.click()
        time.sleep(2)
        print(self.driver.title)
        search_box = self.driver.find_element(By.ID, self.search_box_loc)
        action.click(search_box).key_down(Keys.SHIFT).send_keys("Neve Studio Dance Jacket").key_up(Keys.SHIFT).send_keys(Keys.ENTER).perform()
        time.sleep(3)
        print(self.driver.title)
        assert "NEVE STUDIO" in self.driver.title

