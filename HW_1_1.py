# data input by user
number1 = int(input("enter a first integer: "))
number2 = int(input("enter a second integer: "))
number3 = int(input("enter a third integer: "))
number4 = int(input("enter a fourth integer: "))
number5 = int(input("enter a fifth integer: "))

# find min, max, average
minimum = min(number1, number2, number3, number4, number5)
maximum = max(number1, number2, number3, number4, number5)
average = (number1 + number2 + number3 + number4 + number5) / 5

# print results
print(f"Min: {minimum}")
print(f"Max: {maximum}")
print(f"Average: {average}")