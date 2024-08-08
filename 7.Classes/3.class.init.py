class Person:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

p1=Person("\n\tJohn",36,[100000])
print(p1.name,p1.age,p1.salary)