from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

class CartPage(BasePage):
    """Page Object для страницы корзины."""
    
    CHECKOUT_BUTTON = (By.ID, "checkout")
    
    @allure.step("Начать оформление заказа")
    def checkout(self) -> None:
        """Нажимает кнопку 'Checkout' для начала оформления заказа."""
        self.click_element(self.CHECKOUT_BUTTON)