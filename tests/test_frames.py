from selenium import webdriver
from selenium.webdriver.common.by import By


__url = 'https://demoqa.com/frames'
iframe_selector = '#frame1'
title_selector = '#sampleHeading'
expected_iframe_title = 'This is a sample page'


'''
If you need to interact with elements that locate in frames, you need:
1. Get iframe locator
2. Switch to selected iframe
3. Interact with elements into iframe
4. To leave an iframe or frameset, switch back to the default content like so:
    driver.switch_to.default_content()
'''
# https://www.selenium.dev/documentation/webdriver/browser/frames/


def test_switch_to_iframe(driver):
    driver.get(__url)
    iframe = driver.find_element(By.CSS_SELECTOR, iframe_selector)
    driver.switch_to.frame(iframe)
    title = driver.find_element(By.CSS_SELECTOR, title_selector).text
    assert title == expected_iframe_title


