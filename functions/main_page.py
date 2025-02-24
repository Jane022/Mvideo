
from pages.main_page import MainPage


def product_search(driver, search_data):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search_input_field().send_keys(search_data)
    main_page.search_button().click()