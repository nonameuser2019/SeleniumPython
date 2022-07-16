from time import sleep

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from selenium.common.exceptions import UnexpectedAlertPresentException
import logging


class AllertPage(BasePage):
    alert_btn_locator = "//span[text()='Alerts']"
    allert_block_locator = "//div[@id='javascriptAlertsWrapper']"
    see_alert_btn_locator = "//button[@id='alertButton']"

    logging.basicConfig(filename='logs.log', format='%(asctime)s %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    def allert_block_is_present(self):
        assert self.find_element(By.XPATH, self.allert_block_locator)
        self.logger.info(f'Check that element {self.allert_block_locator} is present')

    def click_on_alert_block(self):
        web_element = self.find_element(By.XPATH, self.alert_btn_locator)
        self.click_on_element(web_element)

    def to_see_alert(self):
        web_element = self.find_element(By.XPATH, self.see_alert_btn_locator)
        self.click_on_element(web_element)

    def check_alert_text(self, text):
        try:
            alert = self.driver.switch_to.alert
            assert alert.text == text, 'Wrong allert text'
        except UnexpectedAlertPresentException:
            pass