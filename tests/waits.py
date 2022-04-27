from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

'''
    1.Before use waits you need to import 2 classes that you can see above
    2.Use WebDriverWait class with 2 params
    3.Use expected_conditions class or you can write your own func and use with until method
'''



__url = 'https://demoqa.com/dynamic-properties'

enable_after_btn_loc = '#enableAfter'
visible_after_btn_loc = '#visibleAfter'


def test_wait_enable_btn(browser):
    browser.get(__url)
    WebDriverWait(browser, 5)\
        .until(EC.element_to_be_clickable(browser.find_element(By.CSS_SELECTOR, enable_after_btn_loc))).click()


def test_until_btn_will_be_visible(browser):
    browser.get(__url)
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, visible_after_btn_loc)))
    #you need to pay attention on 2 parameters for EC func
    