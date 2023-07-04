"""
Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу.
Вимоги:
-Цифри (0-9).
-лише латинські літери у великому (A-Z) та малому (a-z) регістрах.
-у тілі мейла допустимі лише символи "_" і "-". Але вони не можуть бути першим символом мейлу.
-Символ "-" не може повторюватися.
"""
import re

def validate_email(email):
    pattern = r'^[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*@[A-Za-z0-9]+(?:[-][A-Za-z0-9]+)*(?:[.][A-Za-z0-9]+)+$'
    return re.search(pattern, email) and "--" not in email

email = 'test_123@test-mail.com'
if validate_email(email):
    print('good email')
else:
    print('wrong email')
