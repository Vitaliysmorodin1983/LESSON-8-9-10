import allure
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
class TestStore:
    """Тесты для функциональности интернет-магазина."""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)
    
    @allure.title("Проверка процесса оформления заказа")
    @allure.description("Тест проверяет полный процесс оформления заказа в интернет-магазине.")
    def test_checkout_process(self):
        with allure.step("Открыть сайт магазина"):
            self.driver.get("https://www.saucedemo.com/")
        
        with allure.step("Авторизоваться как standard_user"):
            self.login_page.login("standard_user", "secret_sauce")
        
        with allure.step("Добавить товары в корзину"):
            self.main_page.add_backpack_to_cart()
            self.main_page.add_tshirt_to_cart()
            self.main_page.add_onesie_to_cart()
        
        with allure.step("Перейти в корзину"):
            self.main_page.go_to_cart()
        
        with allure.step("Начать оформление заказа"):
            self.cart_page.checkout()
        
        with allure.step("Заполнить форму данными"):
            self.checkout_page.fill_checkout_form("Иван", "Иванов", "123456")
        
        with allure.step("Проверить итоговую сумму"):
            total_text = self.checkout_page.get_total_amount()
            assert "58.29" in total_text, f"Ожидалась сумма $58.29, но получено: {total_text}"