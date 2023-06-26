'''
Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація - https://en.wikipedia.org/wiki/Memoization .
Використовуйте отриманий механізм для прискорення функції рекурсивного обчислення n - го члена ряду Фібоначчі.
Порівняйте швидкість виконання із просто рекурсивним підходом.
'''
def fibonacci_memoization():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        elif n <= 2:
            result = 1
        else:
            result = fibonacci(n-1) + fibonacci(n-2)
        cache[n] = result
        return result

    return fibonacci

fibonacci = fibonacci_memoization()


print(fibonacci(20))


