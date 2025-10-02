from behave import given, when, then
from pages.search_page import SearchPage

########
# GIVEN
########

@given("I navigate to the Home page")
def step_given_navigate_to_home(context):
    context.search_page = SearchPage(context.page, context.base_url)
    context.search_page.navigate()

########
# WHEN
########

@when("I enter a valid product name in the search bar")
def step_when_enter_valid_product_name(context):
    context.search_page.enter_product_name("Thor Hammer")

@when("I click the X button to clear the search results")
def step_when_clear_search_results(context):
    context.search_page.clear_search()

########
# THEN
########

@then("I should see the Thor search results display")
def step_then_verify_thor_search_results(context):
    context.search_page.verify_search_results("Thor Hammer")

@then("I click the X button to clear the search results")
def step_then_click_clear_search_results(context):
    context.search_page.clear_search()

@then("I should see store list restore to default state")
def step_then_verify_store_list_restored(context):
    # Smart reuse: Use category_page if present (for category features), else search_page
    if hasattr(context, 'category_page'):
        context.category_page.verify_default_state_restored()
    else:
        context.search_page.verify_default_state_restored()