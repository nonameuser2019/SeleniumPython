import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class MainPage(BasePage):
    banner_locator = "//div[@id='app']//a"
    allert_block_locator = "//div[@class='category-cards']/div[3]"

    def banner_is_present(self):
        assert self.find_element(By.XPATH, self.banner_locator), 'Banner did not find on the main page'

    def clock_on_allert_block(self):
        web_element = self.find_element(By.XPATH, self.allert_block_locator)
        self.click_on_element(web_element)