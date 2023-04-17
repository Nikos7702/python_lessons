list = [0, 5, 2, 4, 7, 1, 3, 19]
count = 0
for num in list:
    if num % 2 != 0:
        count += 1
print('Number of odd numbers in the list is:', count)