from constants import MAINPAGE_URL
from locators.locators import SEARCH_INPUT_FIELD, SEARCH_BUTTON
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    PAGE_URL = MAINPAGE_URL

    def search_input_field(self):
        return self.wait().until(EC.element_to_be_clickable(SEARCH_INPUT_FIELD))


    def search_button(self):
        return self.wait().until(EC.element_to_be_clickable(SEARCH_BUTTON))



