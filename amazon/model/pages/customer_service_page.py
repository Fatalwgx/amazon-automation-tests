from selene import command
from selene.support.conditions import be
from selene.support.shared import browser


class CustomerServicePage:
    def __init__(self):
        self.page_header = ...
        self.help_topics_heading = ...

    def open(self):
        browser.open('gp/help/customer/display.html')
        return self

    def verify_page_header(self):
        self.page_header = browser.element('//div[@class="cs-title"]/a[text()="Customer Service"]')
        command.js.scroll_into_view(self.page_header)
        self.page_header.should(be.visible)
        return self

    def verify_help_topics_heading(self):
        self.help_topics_heading = browser.element('//h2[text()="All help topics"]')
        command.js.scroll_into_view(self.help_topics_heading)
        self.help_topics_heading.should(be.visible)
        return self
