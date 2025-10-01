# from playwright.sync_api import Page, expect

# class SearchPage:
#     def __init__(self, page: Page, base_url: str):
#         self.page = page
#         self.base_url = base_url.rstrip("/")
#         self.search_bar = "input[data-test='search-query']"
#         self.search_reset_button = "button[data-test='search-reset']"
#         self.card_title = "h5.card-title"
#         self.card_element = "a.card"
#         self.search_completed_container = "div[data-test='search_completed']"
#         self.xpath_price = "/html/body/app-root/div/app-overview/div[3]/div[2]/div[1]/a/div[3]/span/span"

#     def navigate(self):
#         self.page.goto(self.base_url + "/")
#         expect(self.page).to_have_url(self.base_url + "/", timeout=10000)

#     def enter_product_name(self, product_name: str):
#         self.page.fill(self.search_bar, product_name)
#         expect(self.page.locator(self.search_bar)).to_have_value(product_name, timeout=5000)
#         self.page.press(self.search_bar, "Enter")  # Press Enter to submit search

#     def clear_search(self):
#         self.page.click(self.search_reset_button)
#         expect(self.page.locator(self.search_bar)).to_have_value("")

#     def verify_search_results(self, product_name: str):
#         expect(self.page.locator(f'{self.card_title}:has-text("{product_name}")')).to_be_visible(timeout=5000)
#         expect(self.page.locator(self.xpath_price)).to_have_text('$11.14', timeout=5000)

#     def verify_default_state_restored(self):
#         container = self.page.locator(self.search_completed_container)
#         expect(container.locator(self.card_element)).to_have_count(9, timeout=5000)