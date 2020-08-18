class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee:
    def __init__(self,company,address,title,name,age):
        self.company=company
        self.address=address
        self.title=title
        Person.__init__(self,name,age)

    def printer(self):
        print(f'Name of company is {self.company} and the address is {self.address} and the title is {self.title} and the name of the employee is {self.name} and the age of the employee is {self.age}')

    def getter_company(self):
        print(f'The name of the company is {self.company}')
