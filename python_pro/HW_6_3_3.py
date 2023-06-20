"""
Напишіть генераторну функцію, яка повертатиме прості числа.
Верхня межа діапазону повинна бути задана параметром цієї функції.
"""
def prime_numbers_generator(limit):
    for num in range(2, limit + 1):
        if all(num % divisor != 0 for divisor in range(2, int(num ** 0.5) + 1)):
            yield num

for prime in prime_numbers_generator(20):
    print(prime)


