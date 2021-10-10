#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

numbers = ["Один", "Два", "Три", "Четыре"]
with open('text_4.txt', 'r') as f:
    print(f.read())
    f.seek(0, 0)
    my_file = open('text_4_new.txt', 'w+')
    for i, line in enumerate(f):
        str_line = line.split()
        my_file.write(line.replace(str_line[0], numbers[i]))
    my_file.close()
with open('text_4_new.txt', 'r') as ft:
    print(ft.read())
