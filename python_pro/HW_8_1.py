"""
Напишіть декоратор, який виконує певну дію перед і після виконанням функції.
"""

def my_decorator(func):
    def inner(*args, **kwargs):
        print("Before")

        result = func(*args, **kwargs)
        print("Result:", result)

        print("After")

        return result

    return inner


@my_decorator
def sum_numbers(a, b):
    return a + b

sum_numbers(3, 4)
