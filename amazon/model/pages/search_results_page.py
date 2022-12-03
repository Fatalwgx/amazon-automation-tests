from selene import command
from selene.support.shared import browser


class SearchResultsPage:
    def __init__(self):
        self.element = ...

    def open_product_page(self, query: str):
        self.element = browser.element(f'//span[text()="{query}"]')
        command.js.scroll_into_view(self.element)
        self.element.click()
        return self
