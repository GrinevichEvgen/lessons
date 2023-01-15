"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5), стоп (сброс скорости на 0),
отображение скорости, задний ход (изменение знака скорости).
"""


class Car:
    make = None
    model = None     #атрибуты класса
    year = None
    speed = None

if __name__ == "__main__":

  #методы
    def __init__(self, make , model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def increase_speed(self):
        self.speed += 5

    def decrease_speed(self):
        self.speed -= 5

    def stop(self):
        self.speed = 0

    def reverse(self):
        self.speed *= -1


    def print_speed(self):
        print(self.speed)

