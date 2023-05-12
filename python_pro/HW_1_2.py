"""
Необхідно розробити Python-скрипт, який буде повертати користувачеві меню ресторану.
Зазвичай, меню ресторану містить наступні елементи:
- Категорії страв (наприклад, закуски, основні страви, десерти).
- Страви у кожній категорії.
Основні класи, які необхідно створити для реалізації меню ресторану:
Клас Страва: відповідає за збереження інформації про окрему страву, включаючи її назву, опис та ціну.
Клас Категорія страв: відповідає за збереження страв, які належать до конкретної категорії.
Включає список об'єктів "Страва".
Клас Меню: відповідає за збереження всіх категорій страв та їхнього вмісту. Включає список об'єктів "Категорія страв".
Клас Замовлення: відповідає за збереження списку страв, які замовив клієнт, та їхньої ціни.
"""

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


# Створення страв
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

# Створення категорій страв
category1 = MenuCategory("Zupy", [dish1, dish5, dish10])
category2 = MenuCategory("dania główne", [dish2, dish3, dish4, dish7, dish8, dish9, dish11])
category3 = MenuCategory("Desery", [dish6, dish12])

# Створення меню
menu = Menu([category1, category2, category3])

# Виведення інформації про меню
print(menu)

# Створення замовлення
order = Order()

# Додавання страв до замовлення
order.add_item(dish1)
order.add_item(dish2)

# Виведення замовлення та загальної вартості
print("Замовлення:")
for item in order.items:
    print(item)
print("Загальна вартість:", order.calculate_total(), "грн")

# Видалення страви з замовлення
order.remove_item(dish1)

# Оновлення загальної вартості після видалення
print("Оновлене замовлення:")
for item in order.items:
    print(item)
print("Загальна вартість:", order.calculate_total(), "грн")


