from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators mapped using open source platform saucedemo
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://saucedemo.com"

    def navigate(self):
        self.open_url(self.url)

    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)
