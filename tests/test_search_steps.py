from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import expect
from pages.search_page import SearchPage

scenarios("../features/search.feature")

########
# GIVEN
########

@given("I navigate to the Home page")
def navigate_to_home_page(search_page, load_config):
    expect(search_page.page).to_have_url(load_config["base_url"] + "/", timeout=10000)

########
# WHEN
########

@when("I enter a valid product name in the search bar")
def enter_valid_product_name(search_page):
    search_page.enter_product_name("Thor Hammer")

@when("I click the X button to clear the search results")
def clear_search_results(search_page):
    search_page.clear_search()

########
# THEN
########

@then("I should see the Thor search results display")
def verify_thor_search_results(search_page):
    search_page.verify_search_results("Thor Hammer")

@then("I should see store list restore to default state")
def verify_store_list_restored(search_page):
    search_page.verify_default_state_restored()