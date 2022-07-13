from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from pages.base_page import BasePage

__url = 'https://demoqa.com/sortable'
list_items_loc = '.vertical-list-container>.list-group-item'


def test_drag_and_drop_lines(driver):
    
    driver.get(__url)
    list_items = driver.find_elements(By.CSS_SELECTOR, list_items_loc)
    ActionChains(driver).drag_and_drop(list_items[0], list_items[5]).perform()
    time.sleep(2)
    assert list_items[5].text == 'One'
