"""
Напишіть генераторний вираз для заповнення списку.
Список повинен бути заповнений кубами чисел від 2 до вказаної вами величини.
"""
n = int(input('n='))
y = [i ** 3 for i in range(2, n + 1)]
print(y)