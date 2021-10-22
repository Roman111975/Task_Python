# 2. Создайте собственный класс-исключение, обрабатывающий
# ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в
# качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class MyZeroDivision(Exception):
    def init(self, text):
        self.txt = text


a = int(input("Введите целое число: "))

try:
    if a == 0:
        raise MyZeroDivision("Делить на 0 нельзя!")
    else:
        print(int(100 / a))
except ValueError:
    print("Ошибка в значении типа!")
except MyZeroDivision as mr:
    print(mr)

