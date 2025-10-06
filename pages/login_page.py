from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")
        self.sign_in_link = "[data-test='nav-sign-in']"
        self.email_field = "[data-test='email']"
        self.password_field = "[data-test='password']"
        self.login_button = "[data-test='login-submit']"
        self.error_message = "[data-test='login-error']"
        self.email_error = "[data-test='email-error']"
        self.password_error = "[data-test='password-error']"
        self.forgot_password_link = "[data-test='forgot-password-link']"
        self.forgot_password_field = "input[id='email']"
        self.forgot_password_button = "[data-test='forgot-password-submit']"

    def navigate(self):
        self.page.goto(f"{self.base_url}/auth/login")
        expect(self.page).to_have_url(f"{self.base_url}/auth/login", timeout=10000)

    def enter_valid_credentials(self, email, password):
        self.page.fill(self.email_field, email)
        self.page.fill(self.password_field, password)

    def enter_invalid_credentials(self, email, password):
        self.page.fill(self.email_field, email)
        self.page.fill(self.password_field, password)

    def enter_credentials_without_email(self, password):
        self.page.fill(self.password_field, password)

    def enter_credentials_without_password(self, email):
        self.page.fill(self.email_field, email)

    def submit(self):
        self.page.click(self.login_button, timeout=5000)

    def verify_success(self):
        expect(self.page).to_have_url(f"{self.base_url}/account", timeout=10000)

    def verify_login_error(self):
        expect(self.page.locator(self.error_message)).to_be_visible(timeout=5000)

    def verify_email_error(self):
        expect(self.page.locator(self.email_error)).to_be_visible(timeout=5000)

    def verify_password_error(self):
        expect(self.page.locator(self.password_error)).to_be_visible(timeout=5000)

    def click_forgot_password_link(self):
        self.page.click(self.forgot_password_link)
        expect(self.page).to_have_url(f"{self.base_url}/auth/forgot-password", timeout=10000)

# Password reset functionality

    def request_password_reset(self, email):
        self.page.fill(self.forgot_password_field, email)
        self.page.click(self.forgot_password_button)
    
    def password_reset_message(self):
        expect(self.page.locator('div[role="alert"]')).to_have_text('Your password is successfully updated!', timeout=5000)
    
    def password_reset_invalid_email_error(self):
        expect(self.page.locator('div[id="email-error"]')).to_have_text('The selected email is invalid.', timeout=5000)
    
    def password_reset_no_email_error(self):
        expect(self.page.locator('div[id="email-error"]')).to_have_text('Email is required', timeout=5000)