class InvalidDiscountRate(Exception):
    pass


class Discount:
    def __init__(self, discount_rate):
        if not 0 <= discount_rate <= 100:
            raise InvalidDiscountRate("Discount rate must be between 0 and 100")
        self.discount_rate = discount_rate

    def calculate_discount(self, total_price):
        return total_price * (1 - self.discount_rate / 100)


class RegularDiscount(Discount):
    def __init__(self, discount_rate=5):
        super().__init__(discount_rate)


class SilverDiscount(Discount):
    def __init__(self, discount_rate=10):
        super().__init__(discount_rate)


class GoldDiscount(Discount):
    def __init__(self, discount_rate=20):
        super().__init__(discount_rate)


class Client:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount

    def get_total_price(self, order):
        total_price = order.calculate_total()
        discounted_price = self.discount.calculate_discount(total_price)
        return discounted_price


class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f'{self.name} - {self.price} zl\n{self.description}'


class MenuCategory:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes

    def __str__(self):
        category_info = f"{'*' * 10} {self.name} {'*' * 10}\n"
        for dish in self.dishes:
            category_info += str(dish) + "\n"
        return category_info


class Menu:
    def __init__(self, categories):
        self.categories = categories

    def __str__(self):
        menu_info = 'Menu restauracji „Kołyba”\n\n'
        for category in self.categories:
            menu_info += str(category) + "\n"
        return menu_info


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total


dish1 = Dish("Barszcz czerwony", "Tradycyjna polska zupa buraczkowa", 15)
dish2 = Dish("Pierogi ruskie", "Klasyczne pierogi z nadzieniem z ziemniaków i twarogu", 22)
dish3 = Dish("Kotlet schabowy", "Tradycyjna polska panierowana kotlet schabowy", 42)
dish4 = Dish("Bigos", "Kapusta kiszona, mięso i kiełbasa w tradycyjnym polskim gulaszu", 35)
dish5 = Dish("Żurek", "Kwaszony żur na zakwasie żytnim z białą kiełbasą i jajkiem", 20)
dish6 = Dish("Sernik", "Klasyczny polski sernik z miękkim serem i kruchym spodem", 25)
dish7 = Dish("Placki ziemniaczane", "Cienkie placki ziemniaczane serwowane z gulaszem", 34)
dish8 = Dish("Gołąbki", "Farsz z mięsem i ryżem zawinięty w kapustę", 25)
dish9 = Dish("Łazanki", "Makaronowe kluski z kapustą i kiełbasą", 29)
dish10 = Dish("Zupa pomidorowa", "Zupa pomidorowa z ryżem i śmietaną", 13)
dish11 = Dish("Kiełbasa z grilla", "Tradycyjna polska kiełbasa grillowana", 24)
dish12 = Dish("Szarlotka", "Polskie jabłkowe ciasto z kruszonką", 19)

category1 = MenuCategory("Zupy", [dish1, dish5, dish10])
category2 = MenuCategory("Dania główne", [dish2, dish3, dish4, dish7, dish8, dish9, dish11])
category3 = MenuCategory("Desery", [dish6, dish12])

menu = Menu([category1, category2, category3])

print(menu)

order = Order()

order.add_item(dish1)
order.add_item(dish2)
order.add_item(dish4)
order.add_item(dish7)
order.add_item(dish9)
order.add_item(dish12)

print("Zamawianie:")
for item in order.items:
    print(item)
print("Rachunek:", order.calculate_total(), "zl")

order.remove_item(dish2)

print("Racunek prawidlowy:")
for item in order.items:
    print(item)
print("Rachunek:", order.calculate_total(), "zl")


try:
    regular_client = Client("John", RegularDiscount(discount_rate=105))
    total_price_regular = round(regular_client.get_total_price(order), 2)
    print("Rachunek ze zniżką na karcie Regula:", total_price_regular, "zl")
except InvalidDiscountRate as e:
    print("Invalid discount rate:", str(e))

try:
    silver_client = Client("Emily", SilverDiscount(discount_rate=-5))
    total_price_silver = round(silver_client.get_total_price(order), 2)
    print("Rachunek ze zniżką na karcie Silver:", total_price_silver, "zl")
except InvalidDiscountRate as e:
    print("Invalid discount rate:", str(e))

try:
    gold_client = Client("James", GoldDiscount(discount_rate=120))
    total_price_gold = round(gold_client.get_total_price(order), 2)
    print("Rachunek ze zniżką na karcie Gold:", total_price_gold, "zl")
except InvalidDiscountRate as e:
    print("Invalid discount rate:", str(e))

