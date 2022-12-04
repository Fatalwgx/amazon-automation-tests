import allure

from amazon import app
from amazon.model.data.user import User, Country, Category


def test_add_book_to_cart_happy_path():
    with allure.step('Creating test user data'):
        test_user = User(
            first_name='Test_name',
            last_name='Test_surname',
            email='l.zavodskov@vk.team',
            phone='7XXXXXXXXXX',
            password='Insecurity',
            country=Country.United_Kingdom.value,
            category=Category.Books.value,
            products=[
                'Python Cookbook, Third Edition'
            ]
            # TODO: hide credentials in environmental variables
        )

    with allure.step('Opening front page'):
        (
            app.front_page
            .open()
            # registration can be implemented here, but skipped due to certain restrictions
        )

    with allure.step('Authorizing with test user data'):
        pass
        # Inconsistent part due to random captcha
        # (
        #     app.front_page
        #     .authorize_user(
        #         email=test_user.email,
        #         password=test_user.password
        #     )
        # )

    with allure.step('Changing location'):
        (
            app.front_page
            .switch_country(test_user.country)
            .switch_category(test_user.category)
        )

    with allure.step('Specifying category'):
        (
            app.front_page
            .switch_category(test_user.category)
        )

    with allure.step('Searching for product'):
        (
            app.front_page
            .search_product(test_user.products[0])
        )

    with allure.step('Opening searched product\'s page'):
        (
            app.search_results_page
            .open_product_page(test_user.products[0])
        )

    with allure.step('Adding product to cart'):
        (
            app.product_page
            .add_to_cart()
        )

    with allure.step('Opening cart page'):
        (
            app.base_page
            .go_to_cart()
        )

    with allure.step('Verifying added products\'s presence in cart'):
        (
            app.cart_page
            .verify_added_product(test_user.products[0])
        )
