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

    def navigate(self):
        print(f"DEBUG: Navigating to {self.base_url}/auth/login")
        self.page.goto(f"{self.base_url}/auth/login")
        print(f"DEBUG: Current URL: {self.page.url}")
        expect(self.page).to_have_url(f"{self.base_url}/auth/login", timeout=10000)

    def enter_valid_credentials(self, email, password):
        print(f"DEBUG: Entering valid credentials: {email}, {password}")
        self.page.fill(self.email_field, email)
        self.page.fill(self.password_field, password)

    def enter_invalid_credentials(self, email, password):
        print(f"DEBUG: Entering invalid credentials: {email}, {password}")
        self.page.fill(self.email_field, email)
        self.page.fill(self.password_field, password)

    def enter_credentials_without_email(self, password):
        print(f"DEBUG: Entering credentials without email: {password}")
        self.page.fill(self.password_field, password)

    def enter_credentials_without_password(self, email):
        print(f"DEBUG: Entering credentials without password: {email}")
        self.page.fill(self.email_field, email)

    def submit(self):
        print("DEBUG: Clicking login button")
        self.page.click(self.login_button, timeout=5000)

    def verify_success(self):
        print(f"DEBUG: Verifying redirect to {self.base_url}/account")
        expect(self.page).to_have_url(f"{self.base_url}/account", timeout=10000)

    def verify_login_error(self):
        print("DEBUG: Verifying login error message")
        expect(self.page.locator(self.error_message)).to_be_visible(timeout=5000)

    def verify_email_error(self):
        print("DEBUG: Verifying email error message")
        expect(self.page.locator(self.email_error)).to_be_visible(timeout=5000)

    def verify_password_error(self):
        print("DEBUG: Verifying password error message")
        expect(self.page.locator(self.password_error)).to_be_visible(timeout=5000)