class Employee:
    def __init__(self, name, id, **kwargs):
        self.name = name
        self.id = id

    def get_info(self):
        print(f'Имя сотрудника: {self.name}\nИдентификационный номер: {self.id}')

class Manager(Employee):
    def __init__(self,name, id, department, **kwargs):
        super().__init__(name, id, **kwargs)
        self.department = department

    def manage_project(self):
        print(f'Менеджер {self.name} управляет проектами в отделе {self.department} ')

class Technician(Employee):
    def __init__(self, name, id, specialization, **kwargs):
        super().__init__(name, id, **kwargs)
        self.specialization = specialization


    def perform_maintenance(self):
        print(f'Техник {self.name} выполненяет техническое обслуживание в сфере {self.specialization}')


class TechManager(Manager,Technician):
    def __init__(self,name, id, department,specialization):
        super().__init__(name = name,id = id,department = department,specialization = specialization)
        self.list_employee = []

    def add_employee(self, employee):
        self.list_employee.append(employee.name)

    def get_team_info(self):
        print(self.list_employee)

employee1 = Employee('Alex','id1303-1212')
manager  = Manager('Jane', 'Id-404','New York'  )
techician = Technician('Piter','cars','id-405')
tech_manager = TechManager('Oliver', 'id-984503', 'malibu','home')

tech_manager.add_employee(employee1)
tech_manager.add_employee(manager)
tech_manager.add_employee(techician)

tech_manager.get_team_info()
tech_manager.manage_project()
tech_manager.perform_maintenance()
tech_manager.get_info()


