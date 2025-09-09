import allure
import pytest
from pages.calc_page import CalculatorPage

@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    """Тесты для функциональности калькулятора."""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.calc_page = CalculatorPage(driver)
    
    @allure.title("Проверка работы калькулятора с задержкой")
    @allure.description("Тест проверяет корректность работы калькулятора с установленной задержкой выполнения операций.")
    def test_calculator_with_delay(self):
        with allure.step("Открыть страницу калькулятора"):
            self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
        with allure.step("Установить задержку 45 секунд"):
            self.calc_page.set_delay("45")
        
        with allure.step("Выполнить операцию 7 + 8"):
            self.calc_page.click_number_7()
            self.calc_page.click_plus()
            self.calc_page.click_number_8()
            self.calc_page.click_equals()
        
        with allure.step("Дождаться вычисления результата (до 50 секунд)"):
            self.calc_page.wait_for_calculation(50)
        
        with allure.step("Проверить результат"):
            result = self.calc_page.get_result()
            assert result == "15", f"Ожидался результат 15, но получено {result}"
    
    @allure.title("Проверка операции сложения")
    @allure.description("Тест проверяет базовую операцию сложения в калькуляторе.")
    def test_addition_operation(self):
        with allure.step("Открыть страницу калькулятора"):
            self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
        with allure.step("Выполнить операцию 7 + 8"):
            self.calc_page.click_number_7()
            self.calc_page.click_plus()
            self.calc_page.click_number_8()
            self.calc_page.click_equals()
        
        with allure.step("Дождаться вычисления результата (до 10 секунд)"):
            self.calc_page.wait_for_calculation(10)
        
        with allure.step("Проверить результат"):
            result = self.calc_page.get_result()
            assert result == "15", f"Ожидался результат 15, но получено {result}"