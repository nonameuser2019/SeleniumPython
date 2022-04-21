from selenium import webdriver
from selenium.webdriver.common.by import By


__url = 'https://demoqa.com/browser-windows'
new_tab_btn_loc = '#tabButton'
new_page_title_lco = '#sampleHeading'
new_window_btn_loc = '#windowButton'

'''
    1. Find the the selector of button to open new window or tab.
    2. Click on button
    3. Switch to new window by handle with index 1
    4. Find the relevant information
    5. Assert
'''
# code below works with windows and tabs
# don't forget if you need to return on first tab or window you need to save main_window handle at first


def test_change_tab(browser: webdriver.Chrome):
    browser.get(__url)
    # to get main windows name before work with different windows and tabs
    main_window = browser.current_window_handle
    new_tab_btn = browser.find_element(By.CSS_SELECTOR, new_tab_btn_loc)
    new_tab_btn.click()
    # use handle with index 1
    browser.switch_to.window(browser.window_handles[1])
    title = browser.find_element(By.CSS_SELECTOR, new_page_title_lco).text
    assert title == 'This is a sample page'




