name = input('Enter a name: ')
if name[0].isupper():
    if name.isalpha():
        print('The name is valid')
    else:
        print('Mistake')
