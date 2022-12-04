import os
import pytest

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.support.shared import browser

from amazon import app


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        help='Select browser to run tests',
        choices=['chrome', 'firefox'],
        default='chrome'
    )
    # parser.addoption(
    #     '--browser_version',
    #     help='Specify desired browser version',
    #     choices=['100.0', 'Somemore'],
    #     default='100.0'
    # )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    browser_name = request.config.getoption('--browser')
    # browser_version = request.config.getoption('--browser_version')
    options = Options()

    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options
    )
    browser.config.driver = driver

    browser.config.base_url = 'https://www.amazon.com/'
    browser.config.window_height = '1080'
    browser.config.window_width = '1920'
    browser.config.timeout = 6.0

    yield

    (
        app.attach
        .add_html(browser)
        .add_screenshot(browser)
        .add_logs(browser)
        .add_video(browser)
    )
    browser.quit()
