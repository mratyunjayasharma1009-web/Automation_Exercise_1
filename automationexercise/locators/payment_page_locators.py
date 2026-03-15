from selenium.webdriver.common.by import By


class payment_page_locators:

    Card_name_field = (By.NAME, "name_on_card")
    Card_number_field = (By.NAME, "card_number")
    Cvc_field = (By.NAME, "cvc")

    Expiry_month_field = (By.NAME, "expiry_month")
    Expiry_year_field = (By.NAME, "expiry_year")
    Pay_and_confirm_order_button=(By.ID,"submit")