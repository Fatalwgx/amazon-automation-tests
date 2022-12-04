from amazon.model.pages.base_page import BasePage
from amazon.model.pages.cart_page import CartPage
from amazon.model.pages.customer_service_page import CustomerServicePage
from amazon.model.pages.front_page import FrontPage
from amazon.model.pages.gift_cards_page import GiftCardsPage
from amazon.model.pages.product_page import ProductPage
from amazon.model.pages.search_results_page import SearchResultsPage
from amazon.model.pages.sell_page import SellPage
from amazon.utils.attach import Attach

# def given_opened(url):
#     browser.open(url)
#     ads = ss('')
#     ads.perform(command.js.remove)

base_page = BasePage()
front_page = FrontPage()
product_page = ProductPage()
search_results_page = SearchResultsPage()
cart_page = CartPage()
attach = Attach()
customer_service_page = CustomerServicePage()
gift_cards_page = GiftCardsPage()
sell_page = SellPage()
