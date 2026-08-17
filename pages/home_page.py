from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    Txtbx_User = (By.NAME, "username")
    Txtbx_Pwd = (By.NAME, "password")
    Btn_LogIn = (By.XPATH, "//input[@value='Log In']")
    Link_Solutions = (By.XPATH, "//*[text()='Solutions']")
    Link_AboutUs = (By.XPATH, "//*[text()='About Us']")
    Link_Services = (By.XPATH, "//*[text()='Services']")
    Link_Products = (By.XPATH, "//*[text()='Products']")
    Link_Locations = (By.XPATH, "//*[text()='Locations']")
    Icon_Home = (By.CLASS_NAME, "home")
    Icon_AboutUs = (By.CLASS_NAME, "aboutus")
    Icon_Contact = (By.CLASS_NAME, "contact")
    Lnk_Register = (By.XPATH, "//*[text()='Register']")
    Btn_Register = (By.CSS_SELECTOR, "input[value='Register']")

    main_menu_items_check = False

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_home(self):
        self.open_url(self.URL)

    # def login(self, username, password):
    #     self.enter_text(self.USERNAME_INPUT, username)
    #     self.enter_text(self.PASSWORD_INPUT, password)
    #
    # def click_login(self):
    #     self.click(self.LOGIN_BUTTON)

    def validate_login_elements(self):
        self.element_is_present(self.Txtbx_User)
        self.element_is_present(self.Txtbx_Pwd)
        self.element_is_present(self.Btn_LogIn)

    def validate_main_menu_items(self):
        self.element_is_present(self.Link_Solutions)
        self.element_is_present(self.Link_AboutUs)
        self.element_is_present(self.Link_Services)
        self.element_is_present(self.Link_Products)
        self.element_is_present(self.Link_Locations)
        self.main_menu_items_check = True

    def validate_welcome_section_elements(self):
        self.element_is_present(self.Icon_Home)
        self.element_is_present(self.Icon_AboutUs)
        self.element_is_present(self.Icon_Contact)
        self.main_menu_items_check = True

    def navigate_registration(self):
        self.click_element(self.Lnk_Register)
        self.element_is_present(self.Btn_Register)
