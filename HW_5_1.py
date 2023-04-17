text = input("Enter a text string: ")
count = 0

for i in text:
    if i == "b":
        count += 1

print("The number of 'b' characters in the input text string: ", count)