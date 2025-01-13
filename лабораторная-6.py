class UserAccount:
    def __init__(self, username, email, __password):
        self.username = username
        self.email = email
        self.__password = hash(__password)

    def set_password(self, __new_password):
        self.__password = __new_password
        self.__password = hash(self.__password)
        print(self.__password)

    def check_password(self, password):
        return hash(password) == self.__password


user1 = UserAccount('Elena','lenka@mail.ru','honme1')
print(user1.check_password('honme1'))
user1.set_password('forma2')
print(user1.check_password('forma2'))
print(user1.check_password('honme1'))
##################################################

class Vehicle:
    def __init__(self,make, model):
        self.make = make
        self.model = model

    def get_info(self):
        print(f'Марка автомобиля: {self.make} \nМодель автомобиля: {self.model} ')



class Car(Vehicle):
    def __init__(self, make, model,fuel_type):
        self.fuel_type = fuel_type
        super().__init__(make, model)

    def get_info(self):
        print(f'Марка автомобиля: {self.make} \nМодель автомобиля: {self.model} \nТип топлива: {self.fuel_type}')



car1 = Car('Honda','GR-700','M90')
car1.get_info()
