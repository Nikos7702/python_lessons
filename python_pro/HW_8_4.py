"""
Напишіть декоратор, який вимірює час виконання функції.
"""
import time

def measure_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} was completed {execution_time} seconds")


    return inner


@measure_time
def sum_numbers(a, b):
    return a + b

@measure_time
def multiply_numbers(a, b):
    return a * b

sum_numbers(3, 4)
multiply_numbers(2, 5)


