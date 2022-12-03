import os
import pytest
from amazon.utils import attach
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selene.support.shared import browser


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        help='Select browser to run tests',
        choices=['chrome', 'firefox'],
        default='chrome'
    )
    parser.addoption(
        '--browser_version',
        help='Specify desired browser version',
        choices=['100.0', 'Somemore'], # add more option later
        default='100.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    browser_name = request.config.getoption('--browser')
    browser_version = request.config.getoption('--browser_version')
    # options = ChromeOptions
    #
    # if browser_name == 'chrome':
    #     options = ChromeOptions
    # elif browser_name == 'firefox':
    #     options = FirefoxOptions
    #
    # selenoid_capabilities = {
    #     "browserName": browser_name,
    #     "browserVersion": str(browser_version),
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": True
    #     }
    # }
    #
    # options.capabilities.update(selenoid_capabilities)
    #
    # login = os.getenv('LOGIN')
    # password = os.getenv('PASSWORD')
    #
    # driver = webdriver.Remote(
    #     command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
    #     options=options
    # )
    # browser.config.driver = driver

    browser.config.base_url = 'https://www.amazon.com/'
    browser.config.window_height = '1080'
    browser.config.window_width = '1920'
    browser.config.timeout = 6.0

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
