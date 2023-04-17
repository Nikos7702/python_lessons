user_input = input('текст: ')
my_text = ''
for i in range(len(user_input)):
    if user_input[i] == ' ' and user_input[i-1] == ' ':
        continue
    my_text += user_input[i]
print(my_text)
