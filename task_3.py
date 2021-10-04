#3. Реализовать функцию my_func(), которая принимает
# три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(a, b, c))
    return sum(my_list)


print(my_func(10, 5, 2))
