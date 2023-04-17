number = input('Enter 4 numbers: ')
sum_left = 0
sum_right = 0
for i in range(len(number)):
    if i < len(number) // 2:
        sum_left += int(number[i])
    else:
        sum_right += int(number[i])
if sum_left == sum_right:
    print('happy ticket')
else:
    print('Not happy ticket')