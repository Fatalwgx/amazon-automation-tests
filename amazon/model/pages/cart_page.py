from selene.support.conditions import have
from selene.support.shared.jquery_style import ss


class CartPage:
    def verify_added_product(self, product: str):
        ss('div[id^="span.a-truncate.a-size-medium span.a-truncate-cut"]').element_by(
            have.exact_text(product)
        )
        return self
