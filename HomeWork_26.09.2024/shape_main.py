from Shape import Shape, Square, Rectangle, Ellipse, Circle

shapes = [
    Square('Квадрат', 1, 3, 4),
    Rectangle('Прямоугольник', 1,2,4,5),
    Circle('Круг', 3,5,6),
    Ellipse('Эллипс', 4,5,3,4)
]
a = Shape.load()
print(a)