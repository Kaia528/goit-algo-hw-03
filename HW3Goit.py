
""""
from datetime import datetime


def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.today().date()
        return (current_date - input_date).days
    except (ValueError, TypeError):
        return "Помилка: неправильний формат дати. Використовуйте 'YYYY-MM-DD'."


print(get_days_from_today("2024-02-12"))
print(get_days_from_today("12.02.2024"))
print(get_days_from_today(20240212))
print(get_days_from_today("2025-10-01"))



import random

def get_numbers_ticket(min_value, max_value, quantity):
    if (
        min_value < 1 or
        max_value > 1000 or
        min_value > max_value or
        quantity < 1 or
        quantity > (max_value - min_value + 1)
    ):
        return []

    return sorted(random.sample(range(min_value, max_value + 1), quantity))


lottery_numbers = get_numbers_ticket(1, 49, 5)
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

"""