def next_element(my_sequence):
    elements = my_sequence.split(',')

    diff = int(elements[-1]) - int(elements[-2])
    ratio = int(elements[-1]) // int(elements[-2])
    if int(elements[-1]) - int(elements[-2]) == int(elements[-2]) - int(elements[-3]):
        # arithmetic sequence
        return str(int(elements[-1]) + diff)
    elif int(elements[-1]) // int(elements[-2]) == int(elements[-2]) // int(elements[-3]):
         # sequence geometric
        return str(int(elements[-1]) * ratio)
    else:
        return None


my_sequence = '0,5,10,15,20,25'
result = next_element(my_sequence)
print(result)
