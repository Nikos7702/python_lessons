class Discount:
    def __init__(self, discount_rate):
        if discount_rate < 0 or discount_rate > 1:
            raise ValueError("Discount rate must be between 0 and 1.")
        self.discount_rate = discount_rate

    def calculate_discount(self, total_price):
        return total_price * self.discount_rate


class RegularDiscount(Discount):
    def __init__(self, discount_rate=0.95):
        super().__init__(discount_rate)


class SilverDiscount(Discount):
    def __init__(self, discount_rate=0.9):
        super().__init__(discount_rate)


class GoldDiscount(Discount):
    def __init__(self, discount_rate=0.8):
        super().__init__(discount_rate)
