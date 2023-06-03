class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)



length = int(input("Enter the lenght: "))
width = int(input("Enter the width: "))

rectangle = Rectangle(length, width)
print("Area of rectangle: ", rectangle.area())
print("Perimeter of rectangle: ",rectangle.perimeter())