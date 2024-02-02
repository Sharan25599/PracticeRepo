class Company:
    def assign_name(self,name):
        self.name=name

    def show_name(self):
        return self.name

class Employee(Company):
    def assign_id(self,id):
        self.id=id
    def show_id(self):
        return self.id

class Salary(Employee):
    def assign_sal(self,sal):
        self.sal=sal

    def show_sal(self):
        return self.sal

s1=Salary()
s1.assign_name("ABC")
s1.assign_id(101)
s1.assign_sal(20000)

print(s1.show_name())
print(s1.show_id())
print(s1.show_sal())

