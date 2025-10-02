import os
import yaml  # For loading config.yaml
from datetime import datetime
from playwright.sync_api import sync_playwright

def before_all(context):
    print("before_all: Starting Playwright")
    context.playwright = sync_playwright().start()
    
    # Load config.yaml from root
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.yaml')  # Relative to features/ -> root
    try:
        with open(config_path, 'r') as f:
            context.config = yaml.safe_load(f)
        print(f"before_all: Loaded config from {config_path}")
    except FileNotFoundError:
        raise Exception(f"config.yaml not found at {config_path}")
    except yaml.YAMLError as e:
        raise Exception(f"Error parsing config.yaml: {e}")
    
    context.base_url = context.config['base_url']  # Set for POM
    
    # Create reports/screenshots folder if it doesn't exist
    os.makedirs("reports/screenshots", exist_ok=True)

def after_all(context):
    print("after_all: Stopping Playwright")
    context.playwright.stop()

def before_scenario(context, scenario):
    print(f"before_scenario: Launching browser for {scenario.name}")
    try:
        context.browser = context.playwright.chromium.launch(headless=False)
        context.browser_context = context.browser.new_context(
            viewport={'width': 1920, 'height': 1080}
        )
        context.page = context.browser_context.new_page()
        print("before_scenario: Page created successfully")
    except Exception as e:
        print(f"before_scenario: Error - {e}")
        raise

def after_scenario(context, scenario):
    print(f"after_scenario: Cleaning up for {scenario.name}")
    if scenario.status == "failed" and hasattr(context, 'page'):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reports/screenshots/{scenario.name.replace(' ', '_')}_{timestamp}.png"
        context.page.screenshot(path=filename, full_page=True)
        print(f"Screenshot saved to: {filename}")

        # Attach to Behave report only if supported (e.g., with --format=html)
        try:
            with open(filename, 'rb') as f:
                context.attach(f.read(), 'image/png')
        except AttributeError:
            print("Attach not supported in this Behave configuration; screenshot saved to file only.")
        except Exception as attach_err:
            print(f"Failed to attach screenshot: {attach_err}")

    if hasattr(context, 'browser_context'):
        context.browser_context.close()
    if hasattr(context, 'browser'):
        context.browser.close()