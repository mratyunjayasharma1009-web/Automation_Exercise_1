from locators.Cart_page_locator import cart_Page_Locators
from pages.Base_page import BasePage


class cart_Page(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.locator = cart_Page_Locators()


    def checkout(self):
        self.click(self.locator.Proceed_to_check_button)


    def place_order(self):
        self.click(self.locator.Place_order_button)
