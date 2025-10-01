from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import expect
from pages.category_filter_page import CategoryFilterPage

class CategoryFilterPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")
        # self.sign_in_link = "[data-test='nav-sign-in']"
        # self.email_field = "[data-test='email']"
        # self.password_field = "[data-test='password']"
        # self.login_button = "[data-test='login-submit']"
        # self.error_message = "[data-test='login-error']"
        # self.email_error = "[data-test='email-error']"
        # self.password_error = "[data-test='password-error']"
        # self.forgot_password_link = "[data-test='forgot-password-link']"
        # self.forgot_password_field = "input[id='email']"
        # self.forgot_password_button = "[data-test='forgot-password-submit']"