import pytest
import yaml
from pytest_bdd import given, when, then, parsers
from playwright.sync_api import Page, expect

with open("config.yaml", encoding="utf-8") as f:
    CONFIG = yaml.safe_load(f)

# GIVEN
@given('I am on the login page')
def go_to_login_page(page: Page):
    page.goto(CONFIG["base_url"])
    page.click('a[data-test="nav-sign-in"]')
    expect(page).to_have_url("https://practicesoftwaretesting.com/auth/login")

# WHEN
@when('I enter valid credentials')
def enter_valid_credentials(page: Page):
    page.type('input[data-test="email"]', CONFIG["good_email"])
    page.type('input[data-test="password"]', CONFIG["good_pw"])

@when('I click the login button')
def click_login_button(page: Page):
    page.locator('[data-test="login-submit"]').click()

@when('I enter invalid credentials')
def enter_invalid_credentials(page: Page):
    page.type('input[data-test="email"]', CONFIG["bad_email"])
    page.type('input[data-test="password"]', CONFIG["bad_pw"])

@when('I enter credentials without an email')
def enter_credentials_without_email(page: Page):
    page.type('input[data-test="email"]', "")
    page.type('input[data-test="password"]', CONFIG["good_pw"])

@when('I enter credentials without a password')
def enter_credentials_without_password(page: Page):
    page.type('input[data-test="email"]', CONFIG["good_email"])
    page.type('input[data-test="password"]', "")

# THEN
@then('I should be redirected to the account page')
def verify_login_success(page: Page):
    expect(page).to_have_url("https://practicesoftwaretesting.com/account")
    expect(page.locator('[data-test="page-title"]')).to_be_visible()

@then('I should see an error message')
def verify_login_failure(page: Page):
    expect(page.locator('div[data-test="login-error"]')).to_be_visible()
    expect(page.locator('div[class="help-block"]')).to_have_text("Invalid email or password")

@then('I should see the email error message')
def verify_missing_email_error(page: Page):
    expect(page.locator('div[id="email-error"]')).to_be_visible()
    expect(page.locator('div[id="email-error"]')).to_have_text("Email is required")

@then('I should see the password error message')
def verify_missing_password_error(page: Page):
    expect(page.locator('div[id="password-error"]')).to_be_visible()
    expect(page.locator('div[id="password-error"]')).to_have_text("Password is required")