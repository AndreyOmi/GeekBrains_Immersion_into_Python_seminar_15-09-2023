''' 
Задание № 2: 

В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

Задание с проверкой даты:
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
Проверку года на високосность вынести в отдельную защищённую функцию.
'''

'''
 Ответ на задание: создан модуль homework_15-09-2023_task_2.py (вместе с файлом __init__.py)
 Из командной строки перейдите в папку с этим файлом и запустите выражение: 
 python dates_validator_task2.py DD.MM.YYYY 

'''

import argparse

def is_valid_date(date_str):
    day, month, year = map(int, date_str.split('.'))
    
    # Функция, проверяющая является ли год високосным
    def is_leap_year(year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False
    
    # Определение максимально возможного числа в каждом месяце
    max_days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    # Определение выходит ли год за пределы требуемого диапазона 
    if year < 1 or year > 9999:
        return False
    
    # Определение выходит ли месяц за пределы требуемого диапазона
    if month < 1 or month > 12:
        return False
    
    # Определение выходит ли день за пределы требуемого диапазона
    if day < 1 or day > max_days_in_month[month]:
        return False
    
    # Проверка, является ли февраль високосным
    if month == 2 and day == 29 and is_leap_year(year):
        return True
    
    # Если все проверки прошли
    return day <= max_days_in_month[month]

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Проверка правильности формата даты.")
    parser.add_argument("date", type=str, help="Дата должна быть в формате DD.MM.YYYY")
    args = parser.parse_args()
    
    if is_valid_date(args.date):
        print("Дата указана правильно!")
    else:
        print("Это ошибочная дата!")
