from locators.Home_page_locators import HomePageLocators
from pages.Base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

        super().__init__(driver)
        self.locator=HomePageLocators()

    def add_to_cart(self):

        self.click(self.locator.Add_to_cart)

    def view_cart(self):
        self.click(self.locator.View_cart_link)