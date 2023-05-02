x = [item for item in range(0, 50, 3)]
y = [item for item in range(0, 50, 5)]

res = set(x) & set(y)
print(res)