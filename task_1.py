# 1. Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год». В рамках
# класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу
# «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    @classmethod
    def from_string(cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        if Date.is_date_valid(day, month, year):
            print(f'День: {day}|Месяц: {month}|Год: {year}')
        else:
            print('Data is not valid')

    @staticmethod
    def is_date_valid(day, month, year):
        return day <= 31 and month <= 12 and year <= 3999


Date.from_string('10-09-2012')
Date.from_string('32-13-3000')
Date.from_string('32-09-2012')
Date.from_string('10-13-2012')
