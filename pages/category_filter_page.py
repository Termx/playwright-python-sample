from playwright.sync_api import Page, expect
from pages.search_page import SearchPage  # Inherit for shared selectors (card_title, card_element) and navigate()

class CategoryFilterPage(SearchPage):
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.hammer_checkbox_xpath = "//html/body/app-root/div/app-overview/div[3]/div[1]/fieldset[1]/div[1]/ul/fieldset/div[1]/label/input"
        self.filtered_products_container = "div[data-test='search_completed']"

    def select_hammer_category(self):
        hammer_checkbox = self.page.locator(f"xpath={self.hammer_checkbox_xpath}")
        hammer_checkbox.check()
        expect(hammer_checkbox).to_be_checked(timeout=5000)
        # Wait for network idle + short DOM settle for filter to apply
        self.page.wait_for_load_state('networkidle')
        self.page.wait_for_timeout(1000)
        # Wait for Thor Hammer to appear
        self.page.wait_for_selector(f"{self.card_title}:has-text('Thor Hammer')", timeout=15000)
        print(f"Card count after select: {self.page.locator(self.card_element).count()}")  # Debug

    def unselect_hammer_category(self):
        hammer_checkbox = self.page.locator(f"xpath={self.hammer_checkbox_xpath}")
        hammer_checkbox.uncheck()
        expect(hammer_checkbox).not_to_be_checked(timeout=5000)
        # Wait for network idle + short DOM settle for restore
        self.page.wait_for_load_state('networkidle')
        self.page.wait_for_timeout(1000)
        # Poll until default count restores (global cards)
        self.page.wait_for_function("document.querySelectorAll('a.card').length === 9", timeout=15000)
        print(f"Card count after unselect: {self.page.locator(self.card_element).count()}")  # Debug

    def verify_hammer_products_displayed(self):
        expect(self.page.locator(f'{self.card_title}:has-text("Thor Hammer")')).to_be_visible(timeout=15000)

    def verify_default_state_restored(self):
        expect(self.page.locator(self.card_element)).to_have_count(9, timeout=15000)
        print(f"Final card count in restore: {self.page.locator(self.card_element).count()}")  # Debug