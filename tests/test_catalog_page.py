import re
import time

from functions.catalog_page import scroll_to_footer, sort_by_ascending_price
from functions.main_page import product_search
from pages.catalog_page import CatalogPage
from data import search_data_list, search_data
import pytest
import logging


logger = logging.getLogger(__name__)

@pytest.mark.parametrize("search_data", search_data_list)
def test_check_products_search(driver, search_data):
    """Проверяем работу главной поисковой строки для товаров"""
    catalog_page=CatalogPage(driver)
    product_search(driver,search_data)
    time.sleep(1)
    logger.info('Поиск товара осуществлен корректно - ОК')
    assert search_data in catalog_page.product_title().text.lower(), "Поисковый запрос не найден в названиях товаров"


def test_check_products_quantity_in_search_results(driver):
    """Проверяем, что количество товаров в поле "Найдено ... товаров" совпадает с реальным количеством товара на странице"""
    catalog_page=CatalogPage(driver)
    product_search(driver, search_data)
    scroll_to_footer(driver)
    logger.info('Количество найденных товаров верно - ОК')
    assert len(catalog_page.products_titles()) == catalog_page.products_quantity(), "Количество товаров в поле 'Найденo' не совпадает с количеством товара на странице"

# def test_ascending_price_works_fine(driver):
#     """Проверяем, что фильтр по возрастанию цены работает корректно"""
#     catalog_page = CatalogPage(driver)
#     product_search(driver, search_data)
#     sort_by_ascending_price(driver)
#     prices = catalog_page.all_prices()
#     numbers = [int(''.join(re.findall(r'\d+', price.text))) for price in prices]
#     logger.info('Фильтр по возрастанию цены работает верно - ОК')
#     assert numbers == sorted(numbers), "Цены не отсортированы по возрастанию"





