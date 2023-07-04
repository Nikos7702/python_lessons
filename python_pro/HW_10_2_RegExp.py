"""
Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).
"""
import re
def validator(card_number):
    return bool(re.match(r'^\d{4}-\d{4}-\d{4}-\d{4}$', card_number))

card_number = '1234-5678-9012-3456'
if validator(card_number):
    print("Card accepted")
else:
    print("Wrong card")

