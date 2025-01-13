from symtable import Class

class Book:
    title = 'Маленький принц'
    author = 'Антуан де Сент-Экзюпери'
    year = 1942


    def get_info(self):
        print( f"Название книги: {self.__class__.title}, Автор: {self.__class__.author}, Год издания: {self.__class__.year}")
book1= Book()
book1.get_info()

############################
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def get_radius(self):
        print(self.radius)

    def set_radius(self, new_radius):
        self.radius = new_radius

circle1 = Circle(radius=20)
circle2 = Circle(radius=50)
circle2.get_radius()
circle1.set_radius(78)
circle1.get_radius()
