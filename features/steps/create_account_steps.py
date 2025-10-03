from behave import given, when, then
from playwright.sync_api import Page, expect
from pages.create_account_page import CreateAccountPage

#########
# GIVEN
#########

@given("I navigate to the Create Account page")
def step_given_navigate_to_create_account(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.navigate()

#########
# WHEN
#########

@when("I enter the required account details")
def step_when_enter_required_details(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.enter_new_account_credentials()

@when("I enter the account details without a first name")
def step_when_enter_without_first_name(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.first_name("")
    context.create_account_page.click_register_button()

@when("I enter the account details without a last name")
def step_when_enter_without_last_name(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.last_name("")
    context.create_account_page.click_register_button()

@when("I enter the account details without a DOB")
def step_when_enter_without_dob(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.dob("")
    context.create_account_page.click_register_button()

@when("I enter the account details with an invalid DOB")
def step_when_enter_with_invalid_dob(context):
    context.create_account_page.dob("01-01-1990")
    context.create_account_page.click_register_button()

@when("I enter the account details without a street address")
def step_when_enter_without_street(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.street("")
    context.create_account_page.click_register_button()

@when("I enter the account details without a postal code")
def step_when_enter_without_postal_code(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.postal_code("")
    context.create_account_page.click_register_button()

@when("I enter the account details without a city")
def step_when_enter_without_city(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.city("")
    context.create_account_page.click_register_button()

@when("I enter the account details without a state")
def step_when_enter_without_state(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.state("")
    context.create_account_page.click_register_button()

@when("I enter the account details without a country")
def step_when_enter_without_country(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.click_register_button()

@when("I enter the account details without a phone number")
def step_when_enter_without_phone(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.phone("")
    context.create_account_page.click_register_button()

@when("I enter the account details with an invalid phone number format")
def step_when_enter_with_invalid_phone(context):
    context.create_account_page.phone("555-555-5555")

@when("I enter the account details without an email address")
def step_when_enter_without_email(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.email("")
    context.create_account_page.click_register_button()

@when("I enter the account details with a password less than 6 characters")
def step_when_enter_short_password(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.password("P@ss1")
    context.create_account_page.click_register_button()

@when("I enter the account details without a password")
def step_when_enter_without_password(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.password("")
    context.create_account_page.click_register_button()

@when("I enter the account details with a weak password")
def step_when_enter_weak_password(context):
    expect(context.page.locator('div.strength-bar')).to_be_visible(timeout=5000)
    context.create_account_page.password("1")

@when("I enter the account details with a moderate password")
def step_when_enter_moderate_password(context):
    expect(context.page.locator('div.strength-bar')).to_be_visible(timeout=5000)
    context.create_account_page.password("F1")

@when("I enter the account details with a strong password")
def step_when_enter_strong_password(context):
    expect(context.page.locator('div.strength-bar')).to_be_visible(timeout=5000)
    context.create_account_page.password("F1@")

@when("I enter the account details with a very strong password")
def step_when_enter_very_strong_password(context):
    expect(context.page.locator('div.strength-bar')).to_be_visible(timeout=5000)
    context.create_account_page.password("F1@f")

@when("I enter the account details with an excellent password")
def step_when_enter_excellent_password(context):
    expect(context.page.locator('div.strength-bar')).to_be_visible(timeout=5000)
    context.create_account_page.password("F1@fGe!b")

#########
# THEN
#########

@then("I should be redirected back to the login page")
def step_then_redirect_to_login(context):
    expect(context.page).to_have_url(f"{context.base_url}/auth/register", timeout=5000)

@then('I should see the first name error message "{expected_firstname_text}"')
def step_then_first_name_error(context, expected_firstname_text):
    expect(context.page.locator("div[data-test='first-name-error']")).to_have_text(expected_firstname_text, timeout=5000)

@then('I should see the last name error message "{expected_lastname_text}"')
def step_then_last_name_error(context, expected_lastname_text):
    expect(context.page.locator("div[data-test='last-name-error']")).to_have_text(expected_lastname_text, timeout=5000)

@then('I should see the DOB error message "{expected_dob_text}"')
def step_then_dob_error(context, expected_dob_text):
    expect(context.page.locator("xpath=/html/body/app-root/div/app-register/div/div/div/form/div/div[3]/div/div[2]")).to_have_text(expected_dob_text, timeout=5000)

@then('I should see the invalid DOB error message "{expected_invalid_dob_text}"')
def step_then_invalid_dob_error(context, expected_invalid_dob_text):
    expect(context.page.locator("div[data-test='dob-error']")).to_have_text(expected_invalid_dob_text, timeout=5000)

@then('I should see the street address error message "{expected_street_text}"')
def step_then_street_error(context, expected_street_text):
    expect(context.page.locator("div[data-test='street-error']")).to_have_text(expected_street_text, timeout=5000)

@then('I should see the postal code error message "{expected_postalcode_text}"')
def step_then_postal_code_error(context, expected_postalcode_text):
    expect(context.page.locator("xpath=/html/body/app-root/div/app-register/div/div/div/form/div/div[5]/div[2]/div")).to_have_text(expected_postalcode_text, timeout=5000)

@then('I should see the city error message "{expected_city_text}"')
def step_then_city_error(context, expected_city_text):
    expect(context.page.locator("div[data-test='city-error']")).to_have_text(expected_city_text, timeout=5000)

@then('I should see the state error message "{expected_state_text}"')
def step_then_state_error(context, expected_state_text):
    expect(context.page.locator("div[data-test='state-error']")).to_have_text(expected_state_text, timeout=5000)

@then('I should see the country error message "{expected_country_text}"')
def step_then_country_error(context, expected_country_text):
    expect(context.page.locator("div[data-test='country-error']")).to_have_text(expected_country_text, timeout=5000)

@then('I should see the phone number error message "{expected_phone_text}"')
def step_then_phone_error(context, expected_phone_text):
    expect(context.page.locator("div[data-test='phone-error']")).to_have_text(expected_phone_text, timeout=5000)

@then('I should see the invalid phone number error message "{expected_invalid_phone_text}"')
def step_then_invalid_phone_error(context, expected_invalid_phone_text):
    expect(context.page.locator("div[data-test='phone-error']")).to_have_text(expected_invalid_phone_text, timeout=5000)

@then('I should see the email address error message "{expected_email_text}"')
def step_then_email_error(context, expected_email_text):
    expect(context.page.locator("div[data-test='email-error']")).to_have_text(expected_email_text, timeout=5000)

@then('I should see the password error message "{expected_password_text}"')
def step_then_password_error(context, expected_password_text):
    expect(context.page.locator("xpath=/html/body/app-root/div/app-register/div/div/div/form/div/div[11]/div[3]/div[1]")).to_have_text(expected_password_text, timeout=5000)

@then('I should see the minimal password error message "{expected_password_text}"')
def step_then_min_password_error(context, expected_password_text):
    expect(context.page.locator("div[data-test='password-error']")).to_have_text(expected_password_text, timeout=5000)

@then('I should see the invalid password error message "{expected_invalid_password_text}"')
def step_then_invalid_password_error(context, expected_invalid_password_text):
    expect(context.page.locator("xpath=/html/body/app-root/div/app-register/div/div/div/form/div/div[11]/div[3]/div[3]")).to_have_text(expected_invalid_password_text, timeout=5000)

@then("I should see at least one number requirement has passed")
def step_then_one_number_req(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.one_number_requirement_passed()

@then('I should see the weak password bar graph of "width: 20%;"')
def step_then_weak_bar(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.weak_label()
    bar_locator = context.create_account_page.password_bar()
    style_value = bar_locator.get_attribute("style", timeout=5000)
    assert "20%" in style_value, f"Expected '20%' in style '{style_value}', but got '{style_value}'"

@then('I should see the moderate password bar graph of "width: 40%;"')
def step_then_moderate_bar(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.moderate_label()
    bar_locator = context.create_account_page.password_bar()
    style_value = bar_locator.get_attribute("style", timeout=5000)
    assert "40%" in style_value, f"Expected '40%' in style '{style_value}', but got '{style_value}'"

@then("I should see at least one special symbol requirement has passed")
def step_then_special_symbol_req(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.one_special_symbol_requirement_passed()

@then('I should see the strong password bar graph of "width: 60%;"')
def step_then_strong_bar(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.strong_label()
    bar_locator = context.create_account_page.password_bar()
    style_value = bar_locator.get_attribute("style", timeout=5000)
    assert "60%" in style_value, f"Expected '60%' in style '{style_value}', but got '{style_value}'"

@then("I should see both uppercase and lowercase letters requirement have passed")
def step_then_upper_lower_req(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.contain_uppercase_and_lowercase_letters()

@then('I should see the very strong password bar graph of "width: 80%;"')
def step_then_very_strong_bar(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.very_strong_label()
    bar_locator = context.create_account_page.password_bar()
    style_value = bar_locator.get_attribute("style", timeout=5000)
    assert "80%" in style_value, f"Expected '80%' in style '{style_value}', but got '{style_value}'"

@then("I should see at least 8 characters long requirement have passed")
def step_then_eight_chars_req(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.least_eight_characters_requirement_passed()

@then('I should see the excellent password bar graph of "width: 100%;"')
def step_then_excellent_bar(context):
    context.create_account_page = CreateAccountPage(context.page, context.base_url)
    context.create_account_page.excellent_label()
    bar_locator = context.create_account_page.password_bar()
    style_value = bar_locator.get_attribute("style", timeout=5000)
    assert "100%" in style_value, f"Expected '100%' in style '{style_value}', but got '{style_value}'"