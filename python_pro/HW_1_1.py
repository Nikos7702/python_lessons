"""
Створіть клас Product для опису товару. У якості атрибутів товару можна використовувати назву, цінц та опис товару.
Створіть декілька інстансів класу Product.
Створіть клас Cart, який буде виступати у якості кошика з товарами певного покупця.
Кошик може містити декілька товарів певної кількості. Реалізуйте метод обчислення вартості кошика.
В усіх класах має бути визначений метод str.
"""
class Product:
    def __init__(self, name: str, price: float, description: str):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"Назва: {self.name}\n Ціна: {self.price} грн\n Опис: {self.description}"


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


product1 = Product("Ноутбук", 20000, "Потужний ноутбук для роботи")
product2 = Product("Смартфон", 10000, "Сучасний смартфон з високоякісною камерою")

print(product1)
print(product2)

cart = Cart()
cart.add_product(product1, 2)
cart.add_product(product2, 1)

# Виведення інформації про кошик та його загальної вартості
print(cart)

