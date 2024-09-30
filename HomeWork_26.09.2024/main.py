from __future__ import annotations

import math
from abc import abstractmethod


class Coordinated:
	def __init__(self, x: float, y: float):
		self._x: float = x
		self._y: float = y

	def distance(self, other: Coordinated) -> float:
		return math.hypot(math.fabs(self._x - other._x), math.fabs(self._y - other._y))


class Figure:
	@abstractmethod
	def __int__(self) -> float:
		raise NotImplementedError('Нужно реализовать метод area класса Figure')

	@abstractmethod
	def perimeter(self) -> float:
		raise NotImplementedError('Нужно реализовать метод area класса Figure')


class Circle(Coordinated, Figure):
	def __init__(self, x: float, y: float, radius: float):
		super().__init__(x, y)
		self._radius: float = radius

	def __int__(self) -> float:
		return math.pi * self._radius ** 2

	def perimeter(self) -> float:
		return 2 * math.pi * self._radius

	def __str__(self):
		return (f'Эта фигура круг c координатами ({self._x}, {self._y}) с площадью - {self.__int__()}'
						f'b периметром - {self.perimeter()}')


class Square(Figure):
	def __init__(self, side: float):
		self._side: float = side

	def __int__(self) -> float:
		return self._side ** 2

	def perimeter(self) -> float:
		return self._side * 4

	def __str__(self):
		return (f'Эта фигура квадрат площадью - {self.__int__()},'
						f' и периметром - {self.perimeter()}')


class Triangle(Figure):
	def __init__(self, leg_1: float, leg_2: float):
		self._leg_1: float = leg_1
		self._leg_2: float = leg_2

	def __int__(self) -> float:
		return (self._leg_1 * self._leg_2) / 2

	def hypotenuse(self):
		return math.fabs(self._leg_1 ** 2 + self._leg_2 ** 2)

	def perimeter(self) -> float:
		return self._leg_1 + self._leg_2 + self.hypotenuse()

	def __str__(self):
		return (f'Эта фигура прямоугольный треугольник площадью - {self.__int__()},'
						f' и периметром - {self.perimeter()}')


class Trapezoid(Figure):
	def __init__(self, side_a: float, side_b: float, side_c: float, side_d: float):
		self._side_a: float = side_a
		self._side_b: float = side_b
		self._side_c: float = side_c
		self._side_d: float = side_d

	def __int__(self) -> float:
		# Полупериметр
		s = (self._side_a + self._side_b + self._side_c + self._side_d) / 2
		# Площадь по формуле Брахмагупты
		area = math.sqrt((s - self._side_a) * (s - self._side_b) * (s - self._side_c) * (s - self._side_d))
		return area

	def perimeter(self) -> float:
		return self._side_a + self._side_b + self._side_c + self._side_d

	def __str__(self):
		return (f'Эта фигура трапеция площадью - {self.__int__()},'
						f' и периметром - {self.perimeter()}')



a = Circle(2, 3, 4)
print(a)
b = Square(5)
print(b)
c = Triangle(3, 4)
print(c)
d = Trapezoid(2,5,4,7)
print(d)
