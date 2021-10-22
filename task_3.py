# 3. Создайте собственный класс-исключение, который должен проверять
# содержимое списка на наличие только чисел. Проверить работу исключения
# на реальном примере. Необходимо запрашивать у пользователя данные и
# заполнять список. Класс-исключение должен контролировать типы данных
# элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются
# бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду “stop”. При этом скрипт завершается,
# сформированный список выводится на экран.
class TextError(Exception):
    def __init__(self, text):
        self.txt = text
array = []
my_list = ''
while True:
    x = input("Input any words or 'q' to exit: ")
    if x == 'q':
        print(array)
        break
    for i in x:
        try:
            if i.isdigit():
                my_list = my_list + str(i)
            else:
                raise TextError("No words")
        except ValueError:
            print(TextError("No words!"))
        except TextError as te:
            print(te)
    array.append(my_list)
print(my_list)
