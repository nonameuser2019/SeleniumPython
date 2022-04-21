class BasePage:
    def __int__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.timeout = timeout

    def open(self):
        self.browser.get(self.url)
