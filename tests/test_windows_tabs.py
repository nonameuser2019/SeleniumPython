from selenium import webdriver
from selenium.webdriver.common.by import By


__url = 'https://demoqa.com/browser-windows'
new_tab_btn_loc = '#tabButton'
new_page_title_lco = '#sampleHeading'
new_window_btn_loc = '#windowButton'
message_btn_loc = '#messageWindowButton'

'''
    1. Find the the selector of button to open new window or tab.
    2. Click on button
    3. Switch to new window by handle with index 1
    4. Find the relevant information
    5. Assert
'''
# code below works with windows and tabs
# don't forget if you need to return on first tab or window you need to save main_window handle at first


def test_change_tab(driver: webdriver.Chrome):
    driver.get(__url)
    # to get main windows name before work with different windows and tabs
    main_window = driver.current_window_handle
    new_tab_btn = driver.find_element(By.CSS_SELECTOR, new_tab_btn_loc)
    new_tab_btn.click()
    # use handle with index 1
    driver.switch_to.window(driver.window_handles[1])
    title = driver.find_element(By.CSS_SELECTOR, new_page_title_lco).text
    assert title == 'This is a sample page'


def test_change_window_message(driver):
    driver.get(__url)
    main_window = driver.current_window_handle
    new_tab_wind_message = driver.find_element(By.CSS_SELECTOR, message_btn_loc)
    new_tab_wind_message.click()
    browser_handles = driver.window_handles
    driver.switch_to.window(browser_handles[1])
    print(browser_handles)
    print(driver.current_window_handle)
    assert len(browser_handles) > 1




