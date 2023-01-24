'''Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
Добавить конструктор класса и инициализировать атрибуты класса значениями переменных.
Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.'''




class Dog:
    height = None
    weight = None
    name = None
    age = None

    def __init__(self, height, weight, name, age):
        self.name = name
        self.weight = weight
        self.height = height
        self.age = age

    def jamp(self):
        print(f"{self.name} is jamping")

    def run(self):
        print(f"{self.name} is running")

    def bark(self):
        print(f"{self.name} is barking")


if __name__ == "__main__":
    dog = Dog(100, 50, "My dog", 10)

    dog.jamp()
    dog.run()
    dog.bark()

    print(dog.name, dog.age, dog.height, dog.weight)