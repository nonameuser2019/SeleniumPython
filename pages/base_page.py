import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, url, driver: webdriver.Chrome):
        self.driver = driver
        self.url = url

    @allure.step('Go to page')
    def navigate_to(self, url):
        self.driver.get(url)

    @allure.step('Find element with wait')
    def find_element(self, method, selector, timeout=5):
        try:
            print(f'Found Element with selector: {selector}')
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((method, selector)))
        except TimeoutException:
            print(f'Element with selector: {selector} was not found during {timeout} seconds')

    @allure.step('Find elements with wait')
    def find_elements(self, method, selector, timeout=5):
        try:
            print(f'Found Elements with selector: {selector}')
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((method, selector)))
        except TimeoutException:
            print(f'Elements with selector: {selector} was not found during {timeout} seconds')

    @allure.step('Click on Element with wait')
    def click_on_element(self, webelement, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(webelement)).click()
