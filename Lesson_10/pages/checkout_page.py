from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

class CheckoutPage(BasePage):
    """Page Object для страницы оформления заказа."""
    
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_AMOUNT = (By.CLASS_NAME, "summary_total_label")
    
    @allure.step("Заполнить форму оформления заказа: имя '{first_name}', фамилия '{last_name}', индекс '{postal_code}'")
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму оформления заказа.
        
        Args:
            first_name: Имя покупателя
            last_name: Фамилия покупателя
            postal_code: Почтовый индекс
        """
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click_element(self.CONTINUE_BUTTON)
    
    @allure.step("Получить итоговую сумму заказа")
    def get_total_amount(self) -> str:
        """
        Получает итоговую сумму заказа.
        
        Returns:
            str: Текст с итоговой суммой
        """
        return self.find_element(self.TOTAL_AMOUNT).text