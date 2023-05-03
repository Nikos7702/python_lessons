def palindrom(start: int, stop: int):
    max_item = 0
    for i in range(start, stop):
        for j in range(start, stop):
            res = str(i * j)
            if res == res[::-1] and int(res) > max_item:
                max_item = int(res)
                numbers = (i, j)
    return max_item, numbers
print(palindrom(100, 1000))