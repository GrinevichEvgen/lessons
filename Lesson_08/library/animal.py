class Animal:

    height = None
    weight = None
    name = None
    age = None

    def __init__(self, height, weight, name, age):
        self.height, self.weight, self.name, self.age = height, weight, name, age

    def jump(self):
        print(f"{self.name} is jumping")

    def run(self):
        print(f"{self.name} is running")

    def change_name(self, name):
        self.name = name