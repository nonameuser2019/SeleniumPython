from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

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


def test_change_tab(remote):
    remote.get(__url)
    # to get main windows name before work with different windows and tabs
    main_window = remote.current_window_handle
    new_tab_btn = remote.find_element(By.CSS_SELECTOR, new_tab_btn_loc)
    new_tab_btn.click()
    # use handle with index 1
    remote.switch_to.window(remote.window_handles[1])
    title = remote.find_element(By.CSS_SELECTOR, new_page_title_lco).text
    assert title == 'This is a sample page'

def test_change_tab1(remote):
    remote.get(__url)
    # to get main windows name before work with different windows and tabs
    main_window = remote.current_window_handle
    new_tab_btn = remote.find_element(By.CSS_SELECTOR, new_tab_btn_loc)
    new_tab_btn.click()
    # use handle with index 1
    remote.switch_to.window(remote.window_handles[1])
    title = remote.find_element(By.CSS_SELECTOR, new_page_title_lco).text
    assert title == 'This is a sample page'

def test_change_tab2(remote):
    remote.get(__url)
    # to get main windows name before work with different windows and tabs
    main_window = remote.current_window_handle
    new_tab_btn = remote.find_element(By.CSS_SELECTOR, new_tab_btn_loc)
    new_tab_btn.click()
    # use handle with index 1
    remote.switch_to.window(remote.window_handles[1])
    title = remote.find_element(By.CSS_SELECTOR, new_page_title_lco).text
    assert title == 'This is a sample page'

def test_change_tab3(remote):
    remote.get(__url)
    # to get main windows name before work with different windows and tabs
    main_window = remote.current_window_handle
    new_tab_btn = remote.find_element(By.CSS_SELECTOR, new_tab_btn_loc)
    new_tab_btn.click()
    # use handle with index 1
    remote.switch_to.window(remote.window_handles[1])
    title = remote.find_element(By.CSS_SELECTOR, new_page_title_lco).text
    assert title == 'This is a sample page'

def test_change_tab4(remote):
    remote.get(__url)
    # to get main windows name before work with different windows and tabs
    main_window = remote.current_window_handle
    new_tab_btn = remote.find_element(By.CSS_SELECTOR, new_tab_btn_loc)
    new_tab_btn.click()
    # use handle with index 1
    remote.switch_to.window(remote.window_handles[1])
    title = remote.find_element(By.CSS_SELECTOR, new_page_title_lco).text
    assert title == 'This is a sample page'

def test_change_tab5(remote):
    remote.get(__url)
    # to get main windows name before work with different windows and tabs
    main_window = remote.current_window_handle
    new_tab_btn = remote.find_element(By.CSS_SELECTOR, new_tab_btn_loc)
    new_tab_btn.click()
    # use handle with index 1
    remote.switch_to.window(remote.window_handles[1])
    title = remote.find_element(By.CSS_SELECTOR, new_page_title_lco).text
    assert title == 'This is a sample page'

def test_change_tab6(remote):
    remote.get(__url)
    # to get main windows name before work with different windows and tabs
    main_window = remote.current_window_handle
    new_tab_btn = remote.find_element(By.CSS_SELECTOR, new_tab_btn_loc)
    new_tab_btn.click()
    # use handle with index 1
    remote.switch_to.window(remote.window_handles[1])
    title = remote.find_element(By.CSS_SELECTOR, new_page_title_lco).text
    assert title == 'This is a sample page'
