"""
Напишіть генераторну функцію, яка повертатиме прості числа.
Верхня межа діапазону повинна бути задана параметром цієї функції.
"""
def prime_numbers_generator(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            yield num

for prime in prime_numbers_generator(20):
    print(prime)
