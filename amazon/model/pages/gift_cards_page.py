from selene import command
from selene.support.conditions import be, have
from selene.support.shared import browser

from amazon import app
from amazon.model.data.user import Country


class GiftCardsPage:
    def __init__(self):
        self.gift_cards_page_header = ...
        self.e_gift_cards_heading = ...
        self.printed_gift_cards_heading = ...
        self.physical_gift_cards_heading = ...

    def open(self):
        browser.open('')
        app.base_page.switch_country(Country.United_Kingdom.value)
        browser.element('//a[text()="Gift Cards"]').click()
        return self

    def verify_page_header(self):
        self.gift_cards_page_header = browser.element('//h1[text()="Shop the perfect gift card"]')
        self.gift_cards_page_header.with_(timeout=6).should(be.present)
        command.js.scroll_into_view(self.gift_cards_page_header)
        self.gift_cards_page_header.should(be.visible)
        return self

    def verify_e_gift_cards(self):
        self.e_gift_cards_heading = browser.element('//h3[text()="eGift cards"]')
        command.js.scroll_into_view(self.e_gift_cards_heading)
        browser.element('//h3[text()="eGift cards"]').should(be.visible)
        return self

    def verify_physical_cards(self):
        self.physical_gift_cards_heading = browser.element('//h3[text()="Physical gift cards"]')
        command.js.scroll_into_view(self.physical_gift_cards_heading)
        self.physical_gift_cards_heading.should(be.visible)
        return self

    def verify_printed_cards(self):
        self.printed_gift_cards_heading = browser.element('//h3[text()="Print at home"]')
        command.js.scroll_into_view(self.printed_gift_cards_heading)
        self.printed_gift_cards_heading.should(be.visible)
        return self
