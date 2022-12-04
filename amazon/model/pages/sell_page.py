from selene import command
from selene.support.conditions import be
from selene.support.shared import browser

from amazon import app
from amazon.model.data.user import Country


class SellPage:
    def __init__(self):
        self.sell_page_header = ...
        self.header_sign_up_button = ...

    def open(self):
        browser.open('')
        app.base_page.switch_country(Country.United_Kingdom.value)
        browser.element('//a[text()="Sell"]').click()
        return self

    def verify_page_header(self):
        self.sell_page_header = browser.element('//h1[text()="Sell on Amazon"]')
        command.js.scroll_into_view(self.sell_page_header)
        self.sell_page_header.should(be.visible)
        return self

    def sign_up_button_is_preset(self):
        self.header_sign_up_button = browser.element('a[data-ld-append="AZRP_SELL_H"]')
        command.js.scroll_into_view(self.header_sign_up_button)
        self.header_sign_up_button.should(be.visible)
        return self
