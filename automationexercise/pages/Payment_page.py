from locators.payment_page_locators import payment_page_locators
from pages.Base_page import BasePage


class Payment_Page(BasePage):
    def __init__(self, driver):
        self.driver = driver

        super().__init__(driver)

        self.locator=payment_page_locators()

    def payment_gateway(self,card_name,card_number,cvc,month,year):
        self.send_keys(self.locator.Card_name_field,card_name)
        self.send_keys(self.locator.Card_number_field,card_number)
        self.send_keys(self.locator.Cvc_field,cvc)
        self.send_keys(self.locator.Expiry_month_field,month)
        self.send_keys(self.locator.Expiry_year_field,year)
        self.click(self.locator.Pay_and_confirm_order_button)
