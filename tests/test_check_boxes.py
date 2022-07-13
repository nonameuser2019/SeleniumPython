
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

from pages.base_page import BasePage
import pytest


class TestCheckBoxes:
    __url = 'https://demoqa.com/checkbox'
    home_arrow_btn_loc = 'button>svg[stroke="currentColor"]'

    def test_select_check_box(self, driver):
        page = BasePage(self.__url, driver)
        page.navigate_to(self.__url)
        home_btn = page.find_elements(By.CSS_SELECTOR, self.home_arrow_btn_loc)[2]
        page.click_on_element(home_btn)
