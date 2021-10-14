#5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних
# класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод
# для каждого экземпляра.
# класс Stationery
class Stationery:
    Stationery_title = "Pen"
    Stationery_title = "Pencil"
    Stationery_title = "Handle"

    def draw(self):
        print("Запуск отрисовки")


# класс Pen, наследующий Stationery
class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом")


# класс Pencil, наследующий Stationery
class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")


# класс Handle, наследующий Stationery
class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")


s = Stationery()
s.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

h = Handle()
h.draw()
