from selenium.webdriver.common.by import By
from selenium import webdriver
import time


__url = 'https://demoqa.com/sortable'
list_items_loc = '.vertical-list-container>.list-group-item'


def test_drag_and_drop_lines(browser):
    
    browser.get(__url)
    list_items = browser.find_elements(By.CSS_SELECTOR, list_items_loc)
    webdriver.ActionChains(browser).drag_and_drop(list_items[0], list_items[5]).perform()
    time.sleep(2)
    assert list_items[5].text == 'One'
