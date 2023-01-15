'''Создать программу, которая импортирует класс из предыдущей задачи,
создает объект и при инициализации устанавливает марку Mercedes, модель E500, год выпуска 2000.
Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран.'''


class Car:

    def __init__(self, make: str, model: str, year: int, speed: int = 0):
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


def main():
    car = Car("Mercedes", "E500", 2000)
    while car.speed < 100:
        car.increase_speed()
        car.print_speed()
    print(car.make, car.model, car.year)


if __name__ == "__main__":
    main()

