import time

import allure

from amazon import app


def test_gift_cards_page_header_is_present():
    with allure.step('Opening gift cards page'):
        (
            app.gift_cards_page
            .open()
        )

    with allure.step('Opening gift cards page'):
        (
            app.gift_cards_page
            .verify_page_header()
        )


def test_e_gift_cards_are_present():
    with allure.step('Opening gift cards page'):
        (
            app.gift_cards_page
            .open()
        )

    with allure.step('Verifying eGift cards heading presence'):
        (
            app.gift_cards_page
            .verify_e_gift_cards()
        )


def test_physical_gift_cards_are_present():
    with allure.step('Opening gift cards page'):
        (
            app.gift_cards_page
            .open()
        )

    with allure.step('Verifying physical cards heading presence'):
        (
            app.gift_cards_page
            .verify_physical_cards()
        )


def test_printed_gift_cards_are_present():
    with allure.step('Opening gift cards page'):
        (
            app.gift_cards_page
            .open()
        )

    with allure.step('Verifying printed cards heading presence'):
        (
            app.gift_cards_page
            .verify_printed_cards()
        )
