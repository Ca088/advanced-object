
class class1:
    def __init__(self):
        self.x=""
    def Enter(self):
        self.x=input("Enter a string:")
     
    def display(self):
        print("You entered:",self.x.upper())

obj1=class1()
obj1.Enter()
obj1.display()
