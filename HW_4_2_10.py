matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
total_sum = 0
for row in matrix:
    print(row)
    total_sum += sum(row)
print('Total sum of matrix elements:', total_sum)