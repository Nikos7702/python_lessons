a = float(input('enter length side A: '))
b = float(input('enter length side B: '))
c = float(input('enter length side C: '))

if a + b > c and a + c > b and b + c > a:
    print('Yes, such a triangle exists')
else:
    print('Mistake')