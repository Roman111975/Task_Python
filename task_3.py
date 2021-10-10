#3. Создать текстовый файл (не программно), построчно
# записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.

dictionary = {}
with open('text_3.txt', 'r') as f:
    for line in f:
        name, cash = line.split()
        dictionary[name] = float(cash)
    for key, value in dictionary.items():
        if value < 20000:
            print(f'Оклад менее 20000: {key} = {dictionary[key]}')
    print(f'Средняя величина дохода {sum(dictionary.values()) / len(dictionary):.2f}')
