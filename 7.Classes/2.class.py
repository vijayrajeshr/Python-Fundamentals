#employee details

class Employee___info:
    
    def __init__(self,emp_id,name,age,salary,role):
        self.emp_id=emp_id
        self.name=name
        self.age=age
        self.salary=salary
        self.role=role
        


employee__1=Employee___info('2303981','Mr.Wick',48,250000,'security')
employee__2=Employee___info('2303982','Bruce Wayne',32,2500000,'CEO')
employee__3=Employee___info('2303983','Jin Sakai',38,150000,'Martial Artist(from Tsushisma)')


print(employee__1)
print(employee__2)
print(employee__3)

        