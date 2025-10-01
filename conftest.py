import pytest
import yaml
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.search_page import SearchPage

@pytest.fixture
def search_page(page, load_config):
    print("DEBUG: Loading search_page fixture")
    search_page = SearchPage(page, load_config["base_url"])
    search_page.navigate()
    return search_page

@pytest.fixture(scope="session")
def playwright():
    print("DEBUG: Loading playwright fixture")
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    print("DEBUG: Loading browser fixture")
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    print("DEBUG: Loading page fixture")
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.set_default_timeout(10000)
    print("DEBUG: Page created")
    yield page
    print("DEBUG: Closing page")
    context.tracing.stop(path="trace.zip")
    context.close()

@pytest.fixture(scope="session", autouse=True)
def load_config():
    print("DEBUG: Loading load_config fixture")
    with open("config.yaml", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config

@pytest.fixture(scope="function")
def login_page(page, load_config):
    print("DEBUG: Loading login_page fixture")
    login_page = LoginPage(page, load_config["base_url"])
    login_page.navigate()
    return login_page

@pytest.hookimpl(tryfirst=True)
def pytest_bdd_before_scenario(request, feature, scenario):
    print(f"\n\n--> Starting Scenario: '{scenario.name}' from Feature: '{feature.name}'")

@pytest.hookimpl(tryfirst=True)
def pytest_bdd_after_scenario(request, feature, scenario):
    print(f"\n<-- Finished Scenario: '{scenario.name}'")