class Employee:
    NAME_COMPANY = None

    def __init__(self, name, position):
        self.name = name
        self.position = position

    @classmethod
    def set_company_name(cls, company_name):
        cls.NAME_COMPANY = company_name
   
    def get_info(self):
        return f'''
        Name: {self.name}
        Position: {self.position}
        Company: {Employee.NAME_COMPANY}
        '''

employee1 = Employee("John", "Manager")

employee2 = Employee("Alice", "Developer")

print(employee1.get_info())

Employee.set_company_name("Google")

print(employee1.get_info())




