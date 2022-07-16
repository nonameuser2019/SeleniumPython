import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.alert_page import AllertPage
from pages.main_page import MainPage


class TestAlerts:
    __url = 'https://demoqa.com/'
    validate_alert_text = 'You clicked a button'

    def test_alert_1(self, driver):
        main_page = MainPage(driver)
        main_page.navigate_to()
        main_page.banner_is_present()
        main_page.clock_on_allert_block()
        alert_page = AllertPage(driver)
        alert_page.click_on_alert_block()
        alert_page.allert_block_is_present()
        alert_page.to_see_alert()
        alert_page.check_alert_text(self.validate_alert_text)
