from dish import Dish

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
