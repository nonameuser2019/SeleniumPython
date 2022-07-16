import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from singleton import Singleton
import logging


class BasePage:
    url = 'https://demoqa.com/'
    logging.basicConfig(filename='logs.log', format='%(asctime)s %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.logger.info(f'Is {__class__.__name__} class instace was created')

    @allure.step('Go to page')
    def navigate_to(self):
        self.driver.get(self.url)
        self.logger.info(f'Navigate to: {self.url}')

    @allure.step('Find element with wait')
    def find_element(self, method, selector, timeout=5):
        try:
            print(f'Found Element with selector: {selector}')
            self.logger.info(f'Find element with selector: {selector}')
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((method, selector)))
        except TimeoutException:
            print(f'Element with selector: {selector} was not found during {timeout} seconds')
            self.logger.info(f'Element with selector: {selector} was not found during {timeout} seconds')

    @allure.step('Find elements with wait')
    def find_elements(self, method, selector, timeout=5):
        try:
            print(f'Found Elements with selector: {selector}')
            self.logger.info(f'Find elements with selector: {selector}')
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((method, selector)))
        except TimeoutException:
            print(f'Elements with selector: {selector} was not found during {timeout} seconds')
            self.logger.info(f'Element with selector: {selector} was not found during {timeout} seconds')

    @allure.step('Click on Element with wait')
    def click_on_element(self, webelement, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(webelement)).click()
            self.logger.info(f'Click on element: {webelement}')
        except TimeoutException:
            self.logger.error(f'Element not clikable')


