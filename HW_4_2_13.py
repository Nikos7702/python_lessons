n = int(input('Enter maximum width of hourglass (must be odd): '))

# first part
for i in range(n, 0, -2):
    print(" " * (n - i), "*" * i)

# second part
for i in range(3, n + 1, 2):
    print(" " * (n - i), "*" * i)