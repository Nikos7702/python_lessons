p = 1000  # base amount
r = 0.1  # rate
# number of years
n1 = 10
n2 = 20
n3 = 30

a1 = p * (1 + r) ** n1
a2 = p * (1 + r) ** n2
a3 = p * (1 + r) ** n3

print('The amount after', n1, 'years will be:', a1)
print('The amount after', n2, 'years will be:', a2)
print('The amount after', n3, 'years will be:', a3)