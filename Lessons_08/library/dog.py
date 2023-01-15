from Lessons_08.library.animal import Animal


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")
