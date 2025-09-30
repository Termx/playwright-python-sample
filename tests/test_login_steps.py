from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage

#print("DEBUG: Loading test_login_steps.py")

scenarios("../features/login.feature")

@given("I am on the login page")
def go_to_login_page(login_page):
    #print("DEBUG: Running 'I am on the login page' step")
    return login_page

@when("I enter valid credentials")
def enter_valid_credentials(login_page, load_config):
    #print("DEBUG: Running 'I enter valid credentials' step")
    login_page.enter_valid_credentials(load_config["good_email"], load_config["good_pw"])
    return login_page

@when("I enter invalid credentials")
def enter_invalid_credentials(login_page, load_config):
    #print("DEBUG: Running 'I enter invalid credentials' step")
    login_page.enter_invalid_credentials(load_config["bad_email"], load_config["bad_pw"])
    return login_page

@when("I enter credentials without an email")
def enter_credentials_without_email(login_page, load_config):
    #print("DEBUG: Running 'I enter credentials without an email' step")
    login_page.enter_credentials_without_email(load_config["good_pw"])
    return login_page

@when("I enter credentials without a password")
def enter_credentials_without_password(login_page, load_config):
    #print("DEBUG: Running 'I enter credentials without a password' step")
    login_page.enter_credentials_without_password(load_config["good_email"])
    return login_page

@when("I click the login button")
def click_login_button(login_page):
    #print("DEBUG: Running 'I click the login button' step")
    login_page.submit()

@then("I should be redirected to the account page")
def verify_login_success(login_page):
    #print("DEBUG: Running 'I should be redirected to the account page' step")
    login_page.verify_success()

@then("I should see an error message")
def verify_login_failure(login_page):
    #print("DEBUG: Running 'I should see an error message' step")
    login_page.verify_login_error()

@then("I should see the email error message")
def verify_missing_email_error(login_page):
    #print("DEBUG: Running 'I should see the email error message' step")
    login_page.verify_email_error()

@then("I should see the password error message")
def verify_missing_password_error(login_page):
    #print("DEBUG: Running 'I should see the password error message' step")
    login_page.verify_password_error()