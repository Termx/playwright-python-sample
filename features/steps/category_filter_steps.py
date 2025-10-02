from behave import given, when, then
from pages.category_filter_page import CategoryFilterPage

#######
# WHEN
#######

@when("I select the Hammer category from the category filter checkbox")
def select_hammer_category(context):
    # Instantiate category_page if not already set (reuses navigated page from shared Given in search_steps.py)
    if not hasattr(context, 'category_page'):
        context.category_page = CategoryFilterPage(context.page, context.base_url)
    context.category_page.select_hammer_category()

@when("I unselect the Hammer category from the category filter checkbox")
def unselect_hammer_category(context):
    context.category_page.unselect_hammer_category()

#######
# THEN
#######

@then("I should see products displayed that are under the Hammer category")
def verify_hammer_products(context):
    context.category_page.verify_hammer_products_displayed()

@then("I unselect the Hammer category from the category filter checkbox")
def then_unselect_hammer_category(context):
    context.category_page.unselect_hammer_category()

# Note: "I should see store list restore to default state" reuses the smart step from search_steps.py