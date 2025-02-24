from selenium.webdriver.common.by import By


SEARCH_INPUT_FIELD = (By.XPATH, '//input[@id="1"]')
SEARCH_BUTTON = (By.XPATH, '//div[@class="search-icon-wrapper"]')
PRODUCTS_TITLES = (By.XPATH, '//a[@data-testid="product-title"]')
PRODUCTS_QUANTITY = (By.XPATH, '//p[contains(text(), "Найден")]')
FOOTER = (By.XPATH, '//div[@class="footer__other-links-section"]')
FILTER_DROPDOWN = (By.XPATH, '//div[@class="product-list-controls__wrapper"]')
ASCENDING_FILTER = (By.XPATH,'//span[contains(text()," Сначала дешевле ")]')
ALL_PRICES = (By.XPATH, '//span[@class="price__main-value"]')