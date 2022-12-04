import time

import selene
from selene.support.conditions import have, be
from selene.support.shared import browser


class DropDown:
    def __init__(self, element: selene.Element):
        self.element = element

    def select(self, elements, option):
        time.sleep(1)
        browser.element('.a-popover-inner').should(be.visible)
        browser.element(".a-dropdown-container").should(be.clickable)
        browser.element(".a-dropdown-container").click()
        browser.element('.a-popover-inner.a-lgtbox-vertical-scroll').should(be.visible)
        browser.all(elements).element_by(
            have.exact_text(option)
        ).click()
        time.sleep(1)
        return self
