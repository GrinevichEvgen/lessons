'''Создать новый класс Cat, который имеет все те же атрибуты что и Dog,
только заменить метод bark на meow.'''

class Cat:
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

    def meow(self):
        print(f"{self.name} is meowning")


if __name__ == "__main__":
    cat = Cat(100, 50, "My cat", 10)

    cat.jamp()
    cat.run()
    cat.meow()

    print(cat.name, cat.age, cat.height, cat.weight)