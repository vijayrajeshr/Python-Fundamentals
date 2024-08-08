class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call_human(self):
        print("Hello, I am Human")  
        print(self.name)
        print(self.age)

x = Human("Vijay", 25)
x.call_human()