from datetime import datetime

def get_days_from_today(date):
    input_date = datetime.strptime(date, "%Y-%m-%d").date()
    today = datetime.today().date()
    delta = today - input_date
    return delta.days
print(get_days_from_today("2023-12-14"))



import random

def get_numbers_ticket(min_value, max_value, quantity):
    if min_value <1 and max_value > 1000 or quantity < 1 and quantity > (max_value - min_value + 1):
        return []

    return sorted(random.sample(range(min_value, max_value + 1), quantity))
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

import re


def normalize_phone(phone_number):

    phone_number = phone_number.strip()

    if phone_number.startswith('+'):
        cleaned = '+' + re.sub(r'\D', '', phone_number[1:])
    else:
        digits = re.sub(r'\D', '', phone_number)
        if digits.startswith('380'):
            cleaned = '+' + digits
        else:
            cleaned = '+38' + digits

    return cleaned


raw_numbers = [
    "067\t\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "   +38(050)123-32-34",
    "  0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11  "
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print("Нормалізовані номери телефонів для SMS-розсилки:")
print(sanitized_numbers)