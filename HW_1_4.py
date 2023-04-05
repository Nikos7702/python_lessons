num = int(input('Enter a three-digit number: '))

hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

print(hundreds)
print(tens)
print(ones)
