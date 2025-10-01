from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import expect
from pages.login_page import LoginPage

scenarios("login.feature")

########
# GIVEN
########

@given("I am on the login page")
def go_to_login_page(login_page):
    return login_page

########
# WHEN
########

@when("I enter valid credentials")
def enter_valid_credentials(login_page, load_config):
    login_page.enter_valid_credentials(load_config["good_email"], load_config["good_pw"])
    login_page.submit()
    return login_page

@when("I enter invalid credentials")
def enter_invalid_credentials(login_page, load_config):
    login_page.enter_invalid_credentials(load_config["bad_email"], load_config["bad_pw"])
    login_page.submit()
    return login_page

@when("I enter credentials without an email")
def enter_credentials_without_email(login_page, load_config):
    login_page.enter_credentials_without_email(load_config["good_pw"])
    login_page.submit()
    return login_page

@when("I enter credentials without a password")
def enter_credentials_without_password(login_page, load_config):
    login_page.enter_credentials_without_password(load_config["good_email"])
    login_page.submit()
    return login_page

@when("I request a password reset")
def request_password_reset(login_page, load_config):
    login_page.click_forgot_password_link()
    login_page.request_password_reset(load_config["good_email"])
    return login_page

@when("I request a password reset with an invalid email")
def request_password_reset_invalid_email(login_page, load_config):
    login_page.click_forgot_password_link()
    login_page.request_password_reset(load_config["bad_email"])
    return login_page

@when("I request a password reset without an email address")
def request_password_reset_no_email(login_page):
    login_page.click_forgot_password_link()
    login_page.request_password_reset("")
    return login_page

########
# THEN
########

@then("I should be redirected to the account page")
def verify_login_success(login_page):
    login_page.verify_success()

@then("I should see an error message")
def verify_login_failure(login_page):
    login_page.verify_login_error()

@then("I should see the email error message")
def verify_missing_email_error(login_page):
    login_page.verify_email_error()

@then("I should see the password error message")
def verify_missing_password_error(login_page):
    login_page.verify_password_error()

@then("I should see a password reset confirmation message")
def verify_password_reset_confirmation(login_page):
    login_page.password_reset_message()

@then("I should see password reset field display an invalid error message")
def verify_password_reset_invalid_email_error(login_page):
    login_page.password_reset_invalid_email_error()

@then("I should see password reset field display an error message")
def verify_password_reset_no_email_error(login_page):
    login_page.password_reset_no_email_error()