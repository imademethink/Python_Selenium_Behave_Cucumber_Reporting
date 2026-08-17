from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class DriverFactory:
    @staticmethod
    def get_driver(browser_name="chrome"):
        browser = browser_name.lower()
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            # Add headless or custom arguments here if needed
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        else:
            raise ValueError(f"Browser '{browser_name}' is not supported.")
