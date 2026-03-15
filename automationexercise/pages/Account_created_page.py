from pages.Base_page import BasePage

from locators.Account_created_locators import AccountCreatedLocators
class Account_created_page(BasePage):
    def __init__(self, driver):
        self.driver = driver

        super().__init__(driver)

        self.locators = AccountCreatedLocators()


    def click_on_continue_button(self):
        self.click(self.locators.Continue_button)

    def verify_account_created_text(self, text):
        self.text(self.locators.Account_created_message)
