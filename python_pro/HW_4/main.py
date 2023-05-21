from discount import RegularDiscount, SilverDiscount, GoldDiscount
from client import Client
from dish import Dish
from menu import Menu, MenuCategory, Order

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

print("Rachunek prawidłowy:")
for item in order.items:
    print(item)
print("Rachunek:", order.calculate_total(), "zl")

try:
    regular_client = Client("John", RegularDiscount(discount_rate=1.2))
except ValueError as e:
    print("Error:", e)

try:
    silver_client = Client("Emily", SilverDiscount(discount_rate=-0.5))
except ValueError as e:
    print("Error:", e)

try:
    gold_client = Client("James", GoldDiscount(discount_rate=1.5))
except ValueError as e:
    print("Error:", e)

regular_client = Client("John", RegularDiscount(discount_rate=0.95))
silver_client = Client("Emily", SilverDiscount(discount_rate=0.9))
gold_client = Client("James", GoldDiscount(discount_rate=0.8))

total_price_regular = round(regular_client.get_total_price(order), 2)
print("Rachunek ze zniżką na karcie Regular:", total_price_regular, "zl")

total_price_silver = round(silver_client.get_total_price(order), 2)
print("Rachunek ze zniżką na karcie Silver:", total_price_silver, "zl")

total_price_gold = round(gold_client.get_total_price(order), 2)
print("Rachunek ze zniżką na karcie Gold:", total_price_gold, "zl")
