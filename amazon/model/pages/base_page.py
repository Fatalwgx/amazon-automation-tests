import time

import selene
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from amazon.model.controls.dropdown import DropDown
from amazon.model.data import user
from amazon.model.data.user import User


class BasePage:
    """
    Mostly navigation bar methods and controls
    """
    def __init__(self):
        self.country = ...
        self.search_bar = ...

    def search_product(self, description: str):
        time.sleep(2)
        browser.config.driver.find_element(By.CSS_SELECTOR, 'input[id="twotabsearchtextbox"]').send_keys(description)
        browser.element('#nav-search-submit-button').click()
        browser.element("div[class$='-results-header']").with_(timeout=10).should(be.visible)
        return self

    def switch_category(self, option: user.Category):
        s('#searchDropdownBox').send_keys(option)
        s(f'//span[@id="nav-search-label-id"][text()="{option}"]')
        return self

    def switch_country(self, country: str):
        browser.element("a[id^='nav-global-location']").click()
        self.country = DropDown(
            element=browser.element("#GLUXCountryListDropdown")
        )
        self.country.select(
            elements="a[id^='GLUXCountryList']",
            option=str(country)
        )
        s("button.a-button-text").click()
        time.sleep(1)
        return self

    def go_to_cart(self):
        s("a[id='nav-cart']").click()
        return self

    def authorize_user(self, email: User.email, password: User.password):
        s("a[id='nav-link-accountList']").click()
        s("input[id='ap_email']").send_keys(email)
        s("input[id='continue']").click()
        s("input[id='ap_password']").send_keys(password)
        s("input[id='signInSubmit']").click()
        try:
            s("a[id='ap-account-fixup-phone-skip-link']").click()
        except NoSuchElementException:
            pass
        return self
