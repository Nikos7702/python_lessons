'''
Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності,
закон якої задається за допомогою функції користувача.
Крім цього параметром генераторної функції повинні бути значення першого члена прогресії та кількість членів,
що видаються послідовностю. Генератор повинен зупинити свою роботу або по досягненню n-го члена,
або при передачі команди на завершення.
'''

def sqrt(item):
    return item ** 0.5


def cube(item):
    return item ** 3


def gen_item(func, start=1, count=10):
    index = 0
    item = start
    while index < count:
        yield func(item)
        index += 1
        item += 1


for item in gen_item(sqrt):
    print(item)


for item in gen_item(cube):
    print(item)