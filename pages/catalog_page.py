import re

from locators.locators import PRODUCTS_TITLES, PRODUCTS_QUANTITY, FOOTER, ALL_PRICES, FILTER_DROPDOWN
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CatalogPage(BasePage):

    def product_title(self):
        return self.wait().until(EC.visibility_of_element_located(PRODUCTS_TITLES))

    def products_quantity(self):
        elements = self.wait().until(EC.visibility_of_element_located(PRODUCTS_QUANTITY)).text
        products_quantity = re.findall(r'\b\d+\b', elements)
        text_products_quantity = ''.join(products_quantity)
        return int(text_products_quantity)

    def products_titles(self):
        return self.wait().until(EC.presence_of_all_elements_located(PRODUCTS_TITLES))

    def footer(self):
        return self.wait().until(EC.visibility_of_element_located(FOOTER))

    def filter_dropdown(self):
        return self.wait().until(EC.visibility_of_element_located(FILTER_DROPDOWN))

    def all_prices(self):
        return self.wait().until(EC.presence_of_all_elements_located(ALL_PRICES))


