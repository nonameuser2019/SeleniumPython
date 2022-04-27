import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--headless', action='store_true', help='enable headless mod for supported browsers.')
    parser.addoption('--executor', default='192.168.0.23')


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('--browser')
    if browser_name == 'chrome':
        print(' \nStart browser chrome for test')
        options = Options()
        #options.headless = True
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        browser.implicitly_wait(5)
    elif browser_name == 'firefox':
        print(' \nStart browser firefox for test')
        fp = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.implicitly_wait(5)
    else:
        raise pytest.UsageError('--browser should be chrome or firefox')
    yield browser
    print('\nBrowser closed for test')

    browser.quit()


@pytest.fixture
def remote(request):
    browser = request.config.getoption('--browser')
    executor = request.config.getoption('--executor')

    driver = webdriver.Remote(
        command_executor=f'http://{executor}:4444/wd/hub',
        desired_capabilities={'browserName': browser}
    )
    driver.implicitly_wait(2)
    driver.maximize_window()
    request.addfinalizer(driver.quit)

    return driver
