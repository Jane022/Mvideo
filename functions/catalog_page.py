from selenium.common import TimeoutException
from locators.locators import FILTER_DROPDOWN, ASCENDING_FILTER, FOOTER
from pages.catalog_page import CatalogPage
from selenium.webdriver.support import expected_conditions as EC


def scroll_to_footer(driver):
    catalog_page = CatalogPage(driver)
    page_height = catalog_page.driver.execute_script("return document.body.scrollHeight")
    step = 2000
    iterations = round(page_height/step)

    for i in range(iterations):
        catalog_page.driver.execute_script(f"window.scrollTo(0, {i * step});")
        try:
            catalog_page.wait().until(EC.presence_of_element_located(FOOTER))
        except TimeoutException:
            print("Footer не найден, продолжаем прокрутку...")


def sort_by_ascending_price(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.wait().until(EC.element_to_be_clickable(FILTER_DROPDOWN)).click()
    catalog_page.wait().until(EC.element_to_be_clickable(ASCENDING_FILTER)).click()






