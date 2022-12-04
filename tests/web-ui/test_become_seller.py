import allure

from amazon import app


def test_sell_page_header_is_present():
    with allure.step('Opening sell page'):
        (
            app.sell_page
            .open()
        )

    with allure.step('Verifying sell page header'):
        (
            app.sell_page
            .verify_page_header()
        )


def test_header_sign_up_button_is_present():
    with allure.step('Openning sell page'):
        (
            app.sell_page
            .open()
        )

    with allure.step('Verifying sell page header'):
        (
            app.sell_page
            .sign_up_button_is_preset()
        )
