height = int(input('Enter height of rectangle: '))
width = int(input('Enter width of rectangle: '))
for i in range(height):
    for j in range(width):
        if i == 0 or i == height-1 or j == 0 or j == width-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()