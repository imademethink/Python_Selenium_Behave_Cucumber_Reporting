from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OpenAccountPage(BasePage):

    Lnk_OpenNewAccount = (By.XPATH, "//a[@href='openaccount.htm']")
    Btn_OpenNewAccount = (By.XPATH, "//input[@value='Open New Account']")
    Labl_AccountOpenSuccess = (By.XPATH, "//*[text()='Account Opened!']")
    Labl_AccountId = (By.ID, "newAccountId")
    Btn_TransferFunds = (By.XPATH, "//*[text()='Transfer Funds']")
    Txtbx_TransferAmount = (By.ID, "amount")
    Btn_Transfer = (By.XPATH, "//input[@type='submit']")
    Labl_TransferComplete = (By.XPATH, "//*[text()='Transfer Complete!']")

    account_open_success = False

    def __init__(self, driver):
        super().__init__(driver)

    def open_new_account(self):
        self.click_element(self.Lnk_OpenNewAccount)
        self.element_is_present(self.Btn_OpenNewAccount)
        self.click_element(self.Btn_OpenNewAccount)

    def new_account_validation(self):
        self.element_is_present(self.Labl_AccountOpenSuccess)
        self.element_is_present(self.Labl_AccountId)
        print(self.get_element_text(self.Labl_AccountId))
        account_open_success = True

    def init_fund_transfer(self, transfer_amount):
        self.click_element(self.Btn_TransferFunds)
        self.element_is_present(self.Txtbx_TransferAmount)
        self.enter_text(self.Txtbx_TransferAmount, transfer_amount)

    def fund_transfer_validation(self):
        self.click_element(self.Btn_Transfer)
        self.element_is_present(self.Labl_TransferComplete)
