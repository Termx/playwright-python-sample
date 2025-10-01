from behave import given, when, then

@given("I launch the browser")
def step_launch_browser(context):
    # Browser setup is already done in environment.py
    pass

@when('I go to "{url}"')
def step_go_to_url(context, url):
    context.page.goto(url)

@then('the page title should contain "{text}"')
def step_check_title(context, text):
    assert text in context.page.title()
