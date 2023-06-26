'''
Реалізуйте генераторну функцію для генерації послідовності дат.
Початкова та кінцеві дати мають бути задані параметрами цієї функції.
'''
from datetime import datetime, timedelta

def date_range_generator(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += timedelta(days=1)

start_date = datetime(2023, 6, 20)
end_date = datetime(2023, 6, 30)

date_gen = date_range_generator(start_date, end_date)

for date in date_gen:
    print(date.strftime("%Y-%m-%d"))
