"""
Напишіть декоратор, який перехоплює та обробляє виключення, що виникають у функції.
"""
def my_exceptions(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print("Exception occurred:", str(e))

    return inner


@my_exceptions
def divide_numbers(a, b):
    return a / b

result1 = divide_numbers(10, 2)
result2 = divide_numbers(10, 0)

print(result1)
print(result2)
