class Shape:
    def calculate_area(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Circle(Shape):
    def __init__(self):
        self.radius = float(input("Enter the radius of the circle: "))

    def calculate_area(self):
        area = 3.14 * self.radius * self.radius
        print("Area of circle:", area)

class Rectangle(Shape):
    def __init__(self):
        self.length = float(input("Enter the length of the rectangle: "))
        self.width = float(input("Enter the width of the rectangle: "))

    def calculate_area(self):
        area = self.length * self.width
        print("Area of rectangle:", area)

class Triangle(Shape):
    def __init__(self):
        self.base = float(input("Enter the base of the triangle: "))
        self.height = float(input("Enter the height of the triangle: "))

    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print("Area of triangle:", area)

def create_shape(shape_type):
    if shape_type == "circle":
        return Circle()
    elif shape_type == "rectangle":
        return Rectangle()
    elif shape_type == "triangle":
        return Triangle()
    else:
        raise ValueError("Unknown shape type")

shape_type = input("Enter the type of shape (circle, rectangle, triangle): ")
shape = create_shape(shape_type)
shape.calculate_area()
