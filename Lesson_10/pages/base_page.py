from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple, Any

class BasePage:
    """Базовый класс для всех страниц с общими методами взаимодействия с элементами."""
    
    def __init__(self, driver: Any) -> None:
        """
        Инициализация базовой страницы.
        
        Args:
            driver: WebDriver instance для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        """
        Находит элемент на странице с ожиданием его появления.
        
        Args:
            locator: Кортеж (By, selector) для поиска элемента
            
        Returns:
            WebElement: Найденный элемент
        """
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click_element(self, locator: Tuple[str, str]) -> None:
        """
        Кликает по элементу после ожидания его кликабельности.
        
        Args:
            locator: Кортеж (By, selector) для поиска элемента
        """
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def enter_text(self, locator: Tuple[str, str], text: str) -> None:
        """
        Вводит текст в поле ввода.
        
        Args:
            locator: Кортеж (By, selector) для поиска элемента
            text: Текст для ввода
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def is_element_visible(self, locator: Tuple[str, str]) -> bool:
        """
        Проверяет видимость элемента на странице.
        
        Args:
            locator: Кортеж (By, selector) для поиска элемента
            
        Returns:
            bool: True если элемент видим, иначе False
        """
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)) is not None
        except:
            return False