# Class with Destructor
class Exam:
    def __init__(self,x,y):
        print("Object Created")
        self.__a=x
        self.__b=y
    def dis(self):
        print(self.__a,self.__b)    
    def __del__(self):
        print("Object Erased")
# End of Class

ar1=Exam(3,4)
ar2=Exam(5,7)
ar1.dis()
ar2.dis()
del ar1
del ar2

