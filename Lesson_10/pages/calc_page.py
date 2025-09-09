from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from .base_page import BasePage
import allure
import time

class CalculatorPage(BasePage):
    """Page Object для страницы калькулятора."""
    
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    NUMBER_BUTTON_7 = (By.XPATH, "//span[text()='7']")
    NUMBER_BUTTON_8 = (By.XPATH, "//span[text()='8']")
    PLUS_BUTTON = (By.XPATH, "//span[text()='+']")
    EQUALS_BUTTON = (By.XPATH, "//span[text()='=']")
    RESULT_FIELD = (By.CSS_SELECTOR, ".screen")
    
    @allure.step("Установить задержку '{delay}' секунд")
    def set_delay(self, delay: str) -> None:
        """
        Устанавливает значение задержки в поле ввода.
        
        Args:
            delay: Значение задержки в секундах
        """
        self.enter_text(self.DELAY_INPUT, delay)
    
    @allure.step("Нажать кнопку '7'")
    def click_number_7(self) -> None:
        """Нажимает кнопку с цифрой 7."""
        self.click_element(self.NUMBER_BUTTON_7)
    
    @allure.step("Нажать кнопку '8'")
    def click_number_8(self) -> None:
        """Нажимает кнопку с цифрой 8."""
        self.click_element(self.NUMBER_BUTTON_8)
    
    @allure.step("Нажать кнопку '+'")
    def click_plus(self) -> None:
        """Нажимает кнопку сложения."""
        self.click_element(self.PLUS_BUTTON)
    
    @allure.step("Нажать кнопку '='")
    def click_equals(self) -> None:
        """Нажимает кнопку равенства."""
        self.click_element(self.EQUALS_BUTTON)
    
    @allure.step("Получить результат вычислений")
    def get_result(self, timeout: int = 60) -> str:
        """
        Получает текст из поля результата с ожиданием вычисления.
        
        Args:
            timeout: Максимальное время ожидания в секундах
            
        Returns:
            str: Текст результата вычислений
        """
        # Ждем, пока результат не станет отличным от текущего выражения
        def result_is_calculated(driver):
            current_text = self.find_element(self.RESULT_FIELD).text
            return current_text not in ['7+8', '7 + 8', ''] and current_text.isdigit()
        
        from selenium.webdriver.support.ui import WebDriverWait
        wait = WebDriverWait(self.driver, timeout)
        wait.until(result_is_calculated)
        
        return self.find_element(self.RESULT_FIELD).text
    
    @allure.step("Дождаться вычисления результата (до {timeout} секунд)")
    def wait_for_calculation(self, timeout: int = 60) -> None:
        """
        Ожидает завершения вычислений.
        
        Args:
            timeout: Максимальное время ожидания в секундах
        """
        self.get_result(timeout)