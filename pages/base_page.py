from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as WW



class BasePage:


    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait (self):
        return WW(self.driver, 10, 1, [TimeoutException, NoSuchElementException])


    def open(self):
        self.driver.get(self.PAGE_URL)

