from discount import Discount
class Client:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount

    def get_total_price(self, order):
        total_price = order.calculate_total()
        discounted_price = self.discount.calculate_discount(total_price)
        return discounted_price
