'''Создать общий класс Animal, содержащий все общие методы классов Dog и Cat.
Унаследовать Dog и Cat от класса Animal и Удалить в дочерних классах те методы,
которые имеются у родительского класса.
Создать объект каждого класса и вызвать все его методы.'''



from Lessons_08.library.cat import Cat
from Lessons_08.library.dog import Dog


if __name__ == "__main__":

    dog = Dog(100, 50, "My Dog", 10)
    dog.bark()

    dog.change_name("New Name")
    dog.bark()

cat = Cat(100, 50, "My Cat", 10)
cat.meow()

