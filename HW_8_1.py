def search1(sequence, item):
    for index, element in enumerate(sequence):
        if element == item:
            return index
    return -1
sequence = [1, 3, 5, 7, 9]
item = 5
print(search1(sequence, item))


