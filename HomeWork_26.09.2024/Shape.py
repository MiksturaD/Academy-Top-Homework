# Задание 3
# Создайте базовый класс Shape для рисования плоских
# фигур.
# Определите методы:
# ■ Show() — вывод на экран информации о фигуре;
# ■ Save() — сохранение фигуры в файл;
# ■ Load() — считывание фигуры из файла.
# Определите производные классы:
# ■ Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
# ■ Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
# ■ Circle — окружность с заданными координатами центра и радиусом;
# ■ Ellipse — эллипс с заданными координатами верхнего
# угла описанного вокруг него прямоугольника со сторонами, параллельными осям координат, и размерами
# этого прямоугольника.
# Создайте список фигур, сохраните фигуры в файл,
# загрузите в другой список и отобразите информацию о
# каждой из фигур.
from __future__ import annotations

from abc import abstractmethod

import self


class Shape:
    def __init__(self, shape_type: str):
        self._shape_type = shape_type

    def __str__(self):
        with open('shapes.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(lines)

    @abstractmethod
    def save(self):
     pass


    @staticmethod
    def load():
        with open('shapes.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(lines)


class Square(Shape):
    def __init__(self, shape_type: str, coord_x: float, coord_y: float, side: float):
        super().__init__(shape_type)
        self._coord_x = coord_x
        self._coord_y = coord_y
        self._side = side
        Square.save(self)

    def __str__(self):
        return  f'Это фигура - {self._shape_type} с координатами {self._coord_x} и {self._coord_y} и стороной {self._side}'

    def save(self):
        with open('shapes.txt', 'a', encoding='utf-8') as f:
           return f.write(f'Фигура - {self._shape_type}, Координата Х - {self._coord_x}, '
                          f'Координата Y - {self._coord_y}, '
                          f'Длина стороны - {self._side}\n')


class Rectangle(Shape):
    def __init__(self, shape_type: str, coord_x: float, coord_y: float, side_a: float, side_b: float):
        super().__init__(shape_type)
        self._coord_x = coord_x
        self._coord_y = coord_y
        self._side_a = side_a
        self._side_b = side_b
        Rectangle.save(self)

    def __str__(self):
        return  (f'Это фигура - {self._shape_type} с координатами {self._coord_x} и {self._coord_y} и сторонами '
                 f'{self._side_a} и {self._side_b}')

    def save(self):
        with open('shapes.txt', 'a', encoding='utf-8') as f:
           return f.write(f'Фигура - {self._shape_type}, Координата Х - {self._coord_x}, '
                          f'Координата Y - {self._coord_y}, '
                          f'Длина сторон - {self._side_a}'
                          f' и {self._side_b}\n')


class Circle(Shape):
    def __init__(self, shape_type: str, coord_x: float, coord_y: float, radius: float):
        super().__init__(shape_type)
        self._coord_x = coord_x
        self._coord_y = coord_y
        self._radius = radius
        Circle.save(self)

    def __str__(self):
        return  (f'Это фигура - {self._shape_type} с координатами {self._coord_x} и {self._coord_y} и '
                 f'радиусом {self._radius}')

    def save(self):
        with open('shapes.txt', 'a', encoding='utf-8') as f:
           return f.write(f'Фигура - {self._shape_type}, Координата Х - {self._coord_x}, '
                          f'Координата Y - {self._coord_y}, '
                          f'радиус - {self._radius}\n')


class Ellipse(Shape):
    def __init__(self, shape_type: str, coord_x: float, coord_y: float, side_a: float, side_b: float):
        super().__init__(shape_type)
        self._coord_x = coord_x
        self._coord_y = coord_y
        self._side_a = side_a
        self._side_b = side_b
        Ellipse.save(self)

    def __str__(self):
        return  (f'Это фигура - {self._shape_type} с координатами {self._coord_x} и {self._coord_y} и сторонами '
                 f'{self._side_a} и {self._side_b}')

    def save(self):
        with open('shapes.txt', 'a', encoding='utf-8') as f:
           return f.write(f'Фигура - {self._shape_type}, Координата Х - {self._coord_x}, '
                          f'Координата Y - {self._coord_y}, '
                          f'Длина сторон - {self._side_a}'
                          f' и {self._side_b}')


