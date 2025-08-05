import pytest
import yaml
from pytest_bdd import scenario
from playwright.sync_api import Page, sync_playwright


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)  # Set headless=False for debugging
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page
    context.tracing.stop(path="trace.zip")
    context.close()

@pytest.fixture(scope="session", autouse=True)
def load_config():
    import yaml
    with open("config.yaml", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config

@pytest.hookimpl(tryfirst=True)
def pytest_bdd_before_scenario(request, feature, scenario):
    print(f"\n\n--> Starting Scenario: '{scenario.name}' from Feature: '{feature.name}'")

@pytest.hookimpl(tryfirst=True)
def pytest_bdd_after_scenario(request, feature, scenario):
    print(f"\n<-- Finished Scenario: '{scenario.name}'")