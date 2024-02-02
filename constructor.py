class Employee:
    def __init__(self,name,age,salary):
        # __init__ method acts as an constructor - Special type of function
     self.name=name
     self.age=age
     self.salary=salary

    def Employee_details(self):
        print("Name of the employee is",self.name)
        print("Age of the employee is", self.age)
        print("Salary of the employee is", self.salary)

e1=Employee("Sharan",25,2000)
e1.Employee_details()
