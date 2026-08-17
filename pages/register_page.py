from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import secrets
import string

class RegisterPage(BasePage):

    Txtbx_FirstName = (By.ID, "customer.firstName")
    Txtbx_LastName = (By.ID, "customer.lastName")
    Txtbx_Address = (By.ID, "customer.address.street")
    Txtbx_City = (By.ID, "customer.address.city")
    Txtbx_State = (By.ID, "customer.address.state")
    Txtbx_Zip = (By.ID, "customer.address.zipCode")
    Txtbx_Phone = (By.ID, "customer.phoneNumber")
    Txtbx_SSN = (By.ID, "customer.ssn")
    Txtbx_UserName = (By.ID, "customer.username")
    Txtbx_Password = (By.ID, "customer.password")
    Txtbx_PasswordAgain = (By.ID, "repeatedPassword")

    Btn_Register = (By.CSS_SELECTOR, "input[value='Register']")
    Btn_LogOut = (By.XPATH, "//*[text()='Log Out']")
    Labl_Account = (By.XPATH, "//*[text()='Your account was created successfully. You are now logged in.']")

    register_success = False

    def __init__(self, driver):
        super().__init__(driver)

    def registration_init(self):
        chars = string.ascii_letters + string.digits
        random_string = ''.join(secrets.choice(chars) for _ in range(10))

        self.hm_global_data = {"username": random_string}
        self.enter_text(self.Txtbx_FirstName, "Jon")
        self.enter_text(self.Txtbx_LastName, "Doe")
        self.enter_text(self.Txtbx_Address, "221 Baker Street")
        self.enter_text(self.Txtbx_City, "Reading")
        self.enter_text(self.Txtbx_State, "NY")
        self.enter_text(self.Txtbx_Zip, "209876")
        self.enter_text(self.Txtbx_Phone, "7777788888")
        self.enter_text(self.Txtbx_SSN, "1122334455")
        self.enter_text(self.Txtbx_UserName, self.hm_global_data["username"])
        self.enter_text(self.Txtbx_Password, "demo")
        self.enter_text(self.Txtbx_PasswordAgain, "demo")

        self.click_element(self.Btn_Register)

        self.element_is_present(self.Btn_LogOut)
        self.element_is_present(self.Labl_Account)

        self.register_success = True
