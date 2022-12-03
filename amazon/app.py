from amazon.model.pages.base_page import BasePage
from amazon.model.pages.cart_page import CartPage
from amazon.model.pages.front_page import FrontPage
from amazon.model.pages.product_page import ProductPage
from amazon.model.pages.search_results_page import SearchResultsPage

# def given_opened(url):
#     browser.open(url)
#     ads = ss('')
#     ads.perform(command.js.remove)

base_page = BasePage()
front_page = FrontPage()
product_page = ProductPage()
search_results_page = SearchResultsPage()
cart_page = CartPage()
