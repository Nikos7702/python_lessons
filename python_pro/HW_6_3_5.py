'''
Реалізуйте генераторну функцію, яка повертатиме елементи послідовності чисел Фібоначчі
'''
def fibonacci(n):
    a, b = 1, 2
    index = 0
    while index < n:
        yield b
        a, b = b, a + b
        index += 1


for i in fibonacci(10):
    print(i)
