from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

class LoginPage(BasePage):
    """Page Object для страницы авторизации."""
    
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    @allure.step("Авторизоваться с логином '{username}' и паролем '{password}'")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию пользователя.
        
        Args:
            username: Логин пользователя
            password: Пароль пользователя
        """
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)