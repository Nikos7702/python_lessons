class InvalidPriceException(Exception):
    pass

class Product:
    def __init__(self, name: str, price: float, description: str):
        if price <= 0:
            raise InvalidPriceException("Ціна товару повинна бути більше нуля")
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"Назва: {self.name}\nЦіна: {self.price} грн\nОпис: {self.description}"
class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity=1):
        self.products.append((product, quantity))

    def calculate_total(self):
        total = 0
        for item in self.products:
            product, quantity = item
            total += product.price * quantity
        return total

    def __str__(self):
        cart_info = "Кошик:\n"
        for item in self.products:
            product, quantity = item
            cart_info += f"Назва: {product.name}, Кількість: {quantity}, Ціна: {product.price} грн\n"
        cart_info += f"Загальна вартість: {self.calculate_total()} грн"
        return cart_info

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.products):
            raise StopIteration
        product, quantity = self.products[self.index]
        self.index += 1
        return product


try:
    product1 = Product("Ноутбук", 20000, "Потужний ноутбук для роботи")
    product2 = Product("Смартфон", 10000, "Сучасний смартфон з високоякісною камерою")
    product3 = Product("Планшет", 15000, "Компактний планшет з великим дисплеєм")
    product4 = Product("Гарнітура", 500, "Бездротова гарнітура зі шумозаглушенням")
except InvalidPriceException as e:
    print("Виникла помилка:", str(e))

print(product1)
print(product2)
print(product3)
print(product4)

cart = Cart()
cart.add_product(product1, 2)
cart.add_product(product2, 1)
cart.add_product(product3, 3)
cart.add_product(product4, 2)

# Виведення інформації про кошик та його загальної вартості
print(cart)
print("*"*10)
# Перебір елементів кошика за допомогою ітераційного протоколу
for product in cart:
    print(product)
