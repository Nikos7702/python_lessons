import math

x = float(input('Input X: '))
y = float(input('Input Y: '))
distance = math.sqrt(x**2 + y**2)
if distance <= 4:
    print('inside the circle')
else:
    print('outside')