'''Создать программу, которая импортирует класс из предыдущей задачи,
создает объект и при инициализации устанавливает марку Mercedes, модель E500, год выпуска 2000.
Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран.'''

from Lessons_08.solution_01 import Car

def main():
    car = Car("Mercedes", "E500", 2000, 0)
    while car.speed < 100:
        car.increase_speed()
        car.print_speed()
    print(car.make, car.model, car.year, car.speed)


if __name__ == "__main__":
    main()

