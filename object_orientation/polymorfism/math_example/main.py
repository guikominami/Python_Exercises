from shape import Square, Circle

s1 = Square(2)
c1 = Circle(2)

shapes = [s1, c1]

for shape in shapes:
    print(shape.area())
    print(shape.perimeter())

