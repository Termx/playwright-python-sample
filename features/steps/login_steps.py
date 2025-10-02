from behave import given, when, then
from pages.login_page import LoginPage

########
# GIVEN
########

@given("I am on the login page")
def step_go_to_login_page(context):
    context.login_page = LoginPage(context.page, context.base_url)
    context.login_page.navigate()

########
# WHEN
########

@when("I enter valid credentials")
def step_enter_valid_credentials(context):
    context.login_page.enter_valid_credentials(context.config["good_email"], context.config["good_pw"])
    context.login_page.submit()

@when("I enter invalid credentials")
def step_enter_invalid_credentials(context):
    context.login_page.enter_invalid_credentials(context.config["bad_email"], context.config["bad_pw"])
    context.login_page.submit()

@when("I enter credentials without an email")
def step_enter_credentials_without_email(context):
    context.login_page.enter_credentials_without_email(context.config["good_pw"])
    context.login_page.submit()

@when("I enter credentials without a password")
def step_enter_credentials_without_password(context):
    context.login_page.enter_credentials_without_password(context.config["good_email"])
    context.login_page.submit()

@when("I request a password reset")
def step_request_password_reset(context):
    context.login_page.click_forgot_password_link()
    context.login_page.request_password_reset(context.config["good_email"])

@when("I request a password reset with an invalid email")
def step_request_password_reset_invalid_email(context):
    context.login_page.click_forgot_password_link()
    context.login_page.request_password_reset(context.config["bad_email"])

@when("I request a password reset without an email address")
def step_request_password_reset_no_email(context):
    context.login_page.click_forgot_password_link()
    context.login_page.request_password_reset("")

########
# THEN
########

@then("I should be redirected to the account page")
def step_verify_login_success(context):
    context.login_page.verify_success()

@then("I should see an error message")
def step_verify_login_failure(context):
    context.login_page.verify_login_error()

@then("I should see the email error message")
def step_verify_missing_email_error(context):
    context.login_page.verify_email_error()

@then("I should see the password error message")
def step_verify_missing_password_error(context):
    context.login_page.verify_password_error()

@then("I should see a password reset confirmation message")
def step_verify_password_reset_confirmation(context):
    context.login_page.password_reset_message()

@then("I should see password reset field display an invalid error message")
def step_verify_password_reset_invalid_email_error(context):
    context.login_page.password_reset_invalid_email_error()

@then("I should see password reset field display an error message")
def step_verify_password_reset_no_email_error(context):
    context.login_page.password_reset_no_email_error()