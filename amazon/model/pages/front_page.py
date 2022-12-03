from selene.support.shared import browser
from amazon import app
from amazon.model.pages.base_page import BasePage


class FrontPage(BasePage):
    def open(self):
        browser.open('')
        # some remove ads method
        return self
