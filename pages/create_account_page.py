from playwright.sync_api import Page, expect

class CreateAccountPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")
        self.register_link = "a[data-test='register-link']"
        self.register_button = "button[data-test='register-submit']"

        self.first_name_input = "input[data-test='first-name']"
        self.last_name_input = "input[data-test='last_name']"
        self.dob_input = "input[data-test='dob']"
        self.street_input = "input[data-test='street']"
        self.postal_code_input = "input[data-test='postal_code']"
        self.city_input = "input[data-test='city']"
        self.state_input = "input[data-test='state']"
        self.country_select = "input[data-test='country']"
        self.phone_input = "input[data-test='phone']"
        self.email_input = "input[data-test='email']"
        self.password_input = "input[data-test='password']"
        # Error selectors
        self.first_name_error = "div[data-test='first-name-error']"
        self.last_name_error = "div[data-test='last-name-error']"
        self.dob_error = "xpath=/html/body/app-root/div/app-register/div/div/div/form/div/div[3]/div/div[2]"
        self.dob_error_invalid = "div[data-test='dob-error']"
        self.street_error = "div[data-test='street-error']"
        self.postal_code_error = "div[data-test='postal_code-error']"
        self.city_error = "div[data-test='city-error']"
        self.state_error = "div[data-test='state-error']"
        self.country_error = "div[data-test='country-error']"
        self.phone_error = "div[data-test='phone-error']"
        self.email_error = "div[data-test='email-error']"
        self.password_error = "xpath=/html/body/app-root/div/app-register/div/div/div/form/div/div[11]/div[3]/div[1]"
        self.password_error_min = "div[data-test='password-error']"
        self.password_error_invalid = "xpath=/html/body/app-register/div/div/div/form/div/div[11]/div[3]/div[3]"
        # Password bar
        self.strength_labels = "div.strength-labels"
        self.password_bar_xpath = "xpath=/html/body/app-root/div/app-register/div/div/div/form/div/div[11]/div[2]/div[2]/div"
        # Password requirements
        self.one_number_req_xpath = "xpath=/html/body/app-root/div/app-register/div/div/div/form/div/div[11]/div[1]/ul/ul/li[3]"
        self.one_special_symbol_req_xpath = "xpath=/html/body/app-root/div/app-register/div/div/div/form/div/div[11]/div[1]/ul/ul/li[4]"
        self.upper_lower_letters_req_xpath = "xpath=/html/body/app-root/div/app-register/div/div/div/form/div/div[11]/div[1]/ul/ul/li[2]"
        self.eight_chars_req_xpath = "xpath=/html/body/app-root/div/app-register/div/div/div/form/div/div[11]/div[1]/ul/ul/li[1]"

    def navigate(self):
        self.page.goto(f"{self.base_url}/auth/register")
        expect(self.page).to_have_url(f"{self.base_url}/auth/register", timeout=10000)

    def register_your_account_button(self):
        self.page.goto(f"{self.base_url}/auth/register")
        self.page.wait_for_load_state('networkidle', timeout=10000)
        expect(self.page.locator(self.register_link)).to_be_visible(timeout=10000)
        #self.page.click(self.register_link, timeout=10000)

    def click_register_button(self):
        self.page.click(self.register_button)

    def enter_new_account_credentials(self):
        expect(self.page.locator('label[for="first_name"]')).to_have_text("First name", timeout=5000)
        self.page.fill("first_name", "Bob")

        expect(self.page.locator('label[for="last_name"]')).to_have_text("Last name", timeout=5000)
        self.page.fill("last_name", "Smith")

        expect(self.page.locator('label[for="dob"]')).to_have_text("Date of Birth *", timeout=5000)
        self.page.fill("dob", "1990-01-01")

        expect(self.page.locator('label[for="street"]')).to_have_text("Street", timeout=5000)
        self.page.fill("street", "2500 E Arizona Biltmore Cir")

        expect(self.page.locator('label[for="postal_code"]')).to_have_text("Postal code", timeout=5000)
        self.page.fill("postal_code", "85016")

        expect(self.page.locator('label[for="city"]')).to_have_text("City", timeout=5000)
        self.page.fill("city", "Phoenix")

        expect(self.page.locator('label[for="state"]')).to_have_text("State", timeout=5000)
        self.page.fill("state", "AZ")

        expect(self.page.locator('label[for="country"]')).to_have_text("Country", timeout=5000)
        self.page.select_option("country", "United States of America (the)")

        expect(self.page.locator('label[for="phone"]')).to_have_text("Phone", timeout=5000)
        self.page.fill("phone", "5555555555")

        expect(self.page.locator('label[for="email"]')).to_have_text("Email address", timeout=5000)
        self.page.fill("email", "bob.smith532@google.com")

        expect(self.page.locator('label[for="password"]')).to_have_text("Password", timeout=5000)
        self.page.fill("password", "%u@_=Ee^~Su2]Ty")

        self.click_register_button()

    def first_name(self, firstname):
        expect(self.page.locator(self.first_name_input)).to_be_visible(timeout=5000)
        self.page.fill(self.first_name_input, firstname)

    def last_name(self, lastname):
        expect(self.page.locator(self.last_name_input)).to_be_visible(timeout=5000)
        self.page.fill(self.last_name_input, lastname)

    def dob(self, dob):
        expect(self.page.locator(self.dob_input)).to_be_visible(timeout=5000)
        self.page.fill(self.dob_input, dob)

    def street(self, street):
        expect(self.page.locator(self.street_input)).to_be_visible(timeout=5000)
        self.page.fill(self.street_input, street)

    def postal_code(self, postal_code):
        expect(self.page.locator(self.postal_code_input)).to_be_visible(timeout=5000)
        self.page.fill(self.postal_code_input, postal_code)

    def city(self, city):
        expect(self.page.locator(self.city_input)).to_be_visible(timeout=5000)
        self.page.fill(self.city_input, city)
    
    def state(self, state):
        expect(self.page.locator(self.state_input)).to_be_visible(timeout=5000)
        self.page.fill(self.state_input, state)

    def phone(self, phone):
        expect(self.page.locator(self.phone_input)).to_be_visible(timeout=5000)
        self.page.fill(self.phone_input, phone)

    def email(self, email):
        expect(self.page.locator(self.email_input)).to_be_visible(timeout=5000)
        self.page.fill(self.email_input, email)

    def password(self, password):
        expect(self.page.locator(self.password_input)).to_be_visible(timeout=5000)
        self.page.fill(self.password_input, password)

    # Password strength

    def password_bar(self):
        return self.page.locator(self.password_bar_xpath)

    def weak_label(self):
        expect(self.page.locator(self.strength_labels).locator("span.active:has-text('Weak')")).to_be_visible(timeout=5000)

    def moderate_label(self):
        expect(self.page.locator(self.strength_labels).locator("span.active:has-text('Moderate')")).to_be_visible(timeout=5000)

    def strong_label(self):
        expect(self.page.locator(self.strength_labels).locator("span.active:has-text('Strong')")).to_be_visible(timeout=5000)

    def very_strong_label(self):
        expect(self.page.locator(self.strength_labels).locator("span.active:has-text('Very Strong')")).to_be_visible(timeout=5000)

    def excellent_label(self):
        expect(self.page.locator(self.strength_labels).locator("span.active:has-text('Excellent')")).to_be_visible(timeout=5000)

    def one_number_requirement_passed(self):
        expect(self.page.locator(self.one_number_req_xpath)).to_have_text("Include at least one number", timeout=5000)

    def one_special_symbol_requirement_passed(self):
        expect(self.page.locator(self.one_special_symbol_req_xpath)).to_have_text("Have at least one special symbol (e.g., @, #, $, etc.)", timeout=5000)

    def contain_uppercase_and_lowercase_letters(self):
        expect(self.page.locator(self.upper_lower_letters_req_xpath)).to_have_text("Contain both uppercase and lowercase letters", timeout=5000)

    def least_eight_characters_requirement_passed(self):
        expect(self.page.locator(self.eight_chars_req_xpath)).to_have_text("Be at least 8 characters long", timeout=5000)