def save_results(func):
    def inner(*args, **kwargs):
        # Виклик функції
        result = func(*args, **kwargs)

        # Збереження результату у файл
        with open("results.txt", "a") as file:
            file.write(f"Function: {func.__name__}\n")
            file.write(f"Result: {result}\n\n")


    return inner


@save_results
def sum_numbers(a, b):
    return a + b

@save_results
def multiply_numbers(a, b):
    return a * b

result1 = sum_numbers(3, 4)
result2 = multiply_numbers(2, 5)

print("Result 1:", result1)
print("Result 2:", result2)
