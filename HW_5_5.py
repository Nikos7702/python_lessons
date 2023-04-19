text = input('Enter text: ')
print(f'Longest word: {max(text.split(), key=len)}')