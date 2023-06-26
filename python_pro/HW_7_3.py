'''
Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне суми елементів отриманого списку.
'''
def new_sum(numbers, func):
    my_numbers = list(map(func, numbers))
    total_sum = sum(my_numbers)
    return total_sum

def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]

result = new_sum(numbers, square)
print(result)
