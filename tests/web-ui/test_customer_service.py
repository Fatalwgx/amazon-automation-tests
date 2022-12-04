import allure

from amazon import app


def test_customer_service_page_header_is_present():
    with allure.step('Opening customer service page'):
        (
            app.customer_service_page
            .open()
        )

    with allure.step('Verifying header name'):
        (
            app.customer_service_page
            .verify_page_header()
        )


def test_customer_service_help_topics_heading_is_present():
    with allure.step('Opening customer service page'):
        (
            app.customer_service_page
            .open()
        )

    with allure.step('Verifying help topics heading presence'):
        (
            app.customer_service_page
            .verify_help_topics_heading()
        )
