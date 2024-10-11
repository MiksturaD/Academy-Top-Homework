# Задача 4: Полиморфизм
from __future__ import annotations

# Описание: Создайте классы Rectangle и Circle.
# Оба класса должны иметь метод get_area(), который возвращает площадь фигуры.
# Реализуйте механизм полиморфизма, который позволяет вызвать метод get_area() для объекта любого класса.
#
# Условия:
#
#  • Класс Rectangle должен принимать длину и ширину, а класс Circle — радиус.
#  • Метод get_area() должен возвращать площадь фигуры.
import math
from abc import abstractmethod, ABC


class Figure:

	@abstractmethod
	def get_area(self):
		raise NotImplementedError('Необходимо ввести метод get_area')


class Rectangle(Figure):
	def __init__(self, side: int):
		self.__side: int = side

	def get_area(self):
		area = self.__side ** 2
		return area

	def __str__(self):
		return f'Квадрат со стороной - {self.__side} и площадью - {Rectangle.get_area(self)}'


class Circle(Figure):
	def __init__(self, radius: int):
		self.__radius: int = radius

	def get_area(self):
		area = math.pi * self.__radius ** 2
		return area

	def __str__(self):
		return f'Круг радиусом - {self.__radius} и площадью - {Circle.get_area(self)}'


rectangle = Rectangle(4)
rectangle.get_area()
print(rectangle)
circle = Circle(4)
circle.get_area()
print(circle)


# Задача 5: Магические методы
#
# Описание: Создайте класс ComplexNumber, который будет представлять комплексное
# число и реализуйте сложение и вычитание комплексных чисел, используя магические
# методы add() и sub().
#
# Условия:
#  • Конструктор должен принимать действительную и мнимую части.
#  • Реализуйте магические методы для сложения и вычитания.


class Complex:
	def __init__(self, real: float, im: float):
		self.__real: float = real
		self.__im: float = im

	def __add__(self, other: Complex) -> Complex:
		return Complex(self.__real + other.__real, self.__im + other.__im)

	def __sub__(self, other: Complex) -> Complex:
		return Complex(self.__real - other.__real, self.__im - other.__im)

	def __str__(self) -> str:
		sign = '+' if self.__im >= 0 else '-'
		return f'{self.__real} {sign} i{math.fabs(self.__im)}'


a = Complex(1, 5)
b = Complex(2, -3)
c = a + b
print(c)


# Задача 6: Инкапсуляция
#
# Описание: Создайте класс Car, который содержит информацию о марке автомобиля, максимальной скорости и текущей скорости.
# Инкапсулируйте переменные с текущей скоростью, чтобы нельзя было напрямую её изменять.
#
# Условия:
#
#  • Создайте конструктор, принимающий марку и максимальную скорость.
#  • Создайте методы для увеличения и уменьшения скорости, контролируя, чтобы скорость не превышала максимальную.
#  • Добавьте метод для отображения текущей скорости.


class Car:
	def __init__(self, brand: str, max_speed: int, speed: int):
		self.brand: str = brand
		self.max_speed: int = max_speed
		self.__speed: int = speed

	def __str__(self):
		return (f'Марка вашей машины - {self.brand}, ее максимальная скорость равна - {self.max_speed},'
						f' а сейчас вы едете со скоростью - {self.__speed}')

	@property
	def speed(self):
		return f'Текущая скорость равна - {self.__speed}'


a = Car('Subaru', 200, 80)
print(a.speed)


# Задача 7: Абстрактные классы
#
# Описание: Создайте абстрактный класс Shape, который имеет абстрактный метод get_area().
# Затем создайте классы Square и Triangle, которые наследуются от этого
# абстрактного класса и реализуют свои версии метода get_area().
#
# Условия:
#
#  • Класс Square должен принимать длину стороны, а класс Triangle — основание и высоту.
#  • Метод get_area() должен возвращать площадь фигуры.


class Shape(ABC):
	@abstractmethod
	def get_area(self):
		raise NotImplementedError('Необходимо переопределить метод get_area')


class Square(Shape, ABC):
	def __init__(self, side: float):
		self._side: float = side

	def get_area(self):
		area = self._side ** 2
		return area


class Triangle(Shape, ABC):
	def __init__(self, side: float, height: float):
		self._side: float = side
		self._height: float = height

	def get_area(self):
		area = 0.5 * (self._side * self._height)
		return area


s = Square(5)
print(s.get_area())
t = Triangle(4,7)
print((t.get_area()))
