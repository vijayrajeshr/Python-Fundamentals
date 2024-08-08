class Student:
    
    #constructor
    def __init__(self,std_name,std_age):
        self.std_name= std_name
        self.std_age= std_age

#creating object outside the class:
student__1=Student('Vijay',19)
print(student__1.std_name,student__1.std_age)