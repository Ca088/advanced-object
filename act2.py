class rect:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)
w=int(input("Enter width of rectangle: "))
h=int(input("Enter height of rectangle: "))
obj=rect(w,h)
print("The perimeter of rectangle is: ",obj.perimeter())
print("The area of rectangle is: ",obj.area())
