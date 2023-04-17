list = [7, 2, 9, 4]
reversed_list = []
for i in range(len(list)-1, -1, -1):
    reversed_list.append(list[i])
print(reversed_list)