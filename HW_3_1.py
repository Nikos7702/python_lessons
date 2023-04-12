apartment_number = int(input('Enter number of apartment: '))

if apartment_number < 1 or apartment_number > 144:
    print('Wrong number, try again')
else:
    entrance_number = (apartment_number - 1) // 36 + 1
    floor_number = (apartment_number - 1) % 36 // 4 + 1
    apartment_on_floor = (apartment_number - 1) % 4 + 1
    print('Entrance: ', entrance_number)
    print('Floor: ', floor_number)
    print('Appartment on floor: ', apartment_on_floor)