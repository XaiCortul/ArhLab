class Figure:
	def area(self):
    	pass 

class Square(Figure):
	def area(self, side):
    	return side ** 2

class Circle(Figure):
	def area(self, radius):
    	return 3.14 * radius ** 2

# Приклад використання класів
square = Square()
print("Area of square:", square.area(5))

circle = Circle()
print("Area of circle:", circle.area(3))
