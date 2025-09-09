from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

class MainPage(BasePage):
    """Page Object для главной страницы магазина."""
    
    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TSHIRT_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_ONESIE_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    
    @allure.step("Добавить Sauce Labs Backpack в корзину")
    def add_backpack_to_cart(self) -> None:
        """Добавляет товар 'Sauce Labs Backpack' в корзину."""
        self.click_element(self.ADD_BACKPACK_BUTTON)
    
    @allure.step("Добавить Sauce Labs Bolt T-Shirt в корзину")
    def add_tshirt_to_cart(self) -> None:
        """Добавляет товар 'Sauce Labs Bolt T-Shirt' в корзину."""
        self.click_element(self.ADD_TSHIRT_BUTTON)
    
    @allure.step("Добавить Sauce Labs Onesie в корзину")
    def add_onesie_to_cart(self) -> None:
        """Добавляет товар 'Sauce Labs Onesie' в корзину."""
        self.click_element(self.ADD_ONESIE_BUTTON)
    
    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Переходит на страницу корзины."""
        self.click_element(self.CART_BUTTON)