#4. Реализуйте базовый класс Car. У данного класса должны быть
# следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в
# базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} Машина поехала. Скорость {self.speed} km\h.')

    def stop(self):
        self.speed = 0
        print(f'{self.name} Машина остановилась. Скорость {self.speed} km\h.')

    def turn(self, direction):
        print(f'{self.name} Машина повернула на  {direction}')

    def show_speed(self):
        if self.speed >= 40 and self.name == 'Превышение скорости':
            print(f'Превышение скорости{self.speed} km\h for {self.name}')
        elif self.speed >= 60 and self.name == 'ВАЗ-2107':
            print(f'Превышение скорости {self.speed} km\h для {self.name}')
        else:
            print(f'{self.name} скорость {self.speed} km\h')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(60, 'черный', 'ВАЗ-2107', True)
work_car = WorkCar(40, ',белый', 'ВАЗ-2101', True)

town_car.go(), town_car.turn('направо'), town_car.show_speed(), town_car.stop()
work_car.go(), work_car.turn('налево'), work_car.show_speed(), work_car.stop()
