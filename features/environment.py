import os
from datetime import datetime
from playwright.sync_api import sync_playwright

def before_all(context):
    print("before_all: Starting Playwright")  # Debug print
    context.playwright = sync_playwright().start()
    # Create reports/screenshots folder if it doesn't exist
    os.makedirs("reports/screenshots", exist_ok=True)

def after_all(context):
    print("after_all: Stopping Playwright")  # Debug print
    context.playwright.stop()

def before_scenario(context, scenario):
    print(f"before_scenario: Launching browser for {scenario.name}")  # Debug print
    try:
        context.browser = context.playwright.chromium.launch(headless=True)
        context.browser_context = context.browser.new_context()  # Renamed to avoid issues
        context.page = context.browser_context.new_page()
        print("before_scenario: Page created successfully")  # Confirm attachment
    except Exception as e:
        print(f"before_scenario: Error - {e}")
        raise  # Re-raise to fail visibly

def after_scenario(context, scenario):
    print(f"after_scenario: Cleaning up for {scenario.name}")  # Debug print
    if scenario.status == "failed":
        # Timestamped screenshot filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reports/screenshots/{scenario.name.replace(' ', '_')}_{timestamp}.png"
        context.page.screenshot(path=filename, full_page=True)
        print(f"Screenshot saved to: {filename}")

        # Attach to Behave report (replace the old attach line with this)
        def attach_screenshot(attachment_name):
            with open(filename, 'rb') as f:
                return f.read()

        context.attach(filename, "image/png", "Screenshot on Failure")

    if hasattr(context, 'browser_context'):
        context.browser_context.close()
    if hasattr(context, 'browser'):
        context.browser.close()