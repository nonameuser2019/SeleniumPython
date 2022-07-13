import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

from pages.base_page import BasePage
import pytest

'''
    1.Before use waits you need to import 2 classes that you can see above
    2.Use WebDriverWait class with 2 params
    3.Use expected_conditions class or you can write your own func and use with until method
'''


class TestForWaitElements:
    __url = 'https://demoqa.com/dynamic-properties'

    enable_after_btn_loc = '#enableAfter'
    visible_after_btn_loc = '#visibleAfter'

    def test_wait_enable_btn(self, driver):
        page = BasePage(self.__url, driver)
        page.navigate_to(self.__url)
        enable_btn = page.find_element(By.CSS_SELECTOR, self.enable_after_btn_loc)
        page.click_on_element(enable_btn, timeout=5)
