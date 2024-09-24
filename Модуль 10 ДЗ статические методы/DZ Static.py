from __future__ import annotations


# Задание 1
# К уже реализованному классу «Дробь» добавьте статический метод, который
# при вызове возвращает количество созданных объектов класса «Дробь».

# class Fraction:
# 	_count = 0
# 	def __init__(self, numerator: int, denominator: int, int_part: int = 0):
# 		self.__num: int = numerator + int_part * denominator
# 		self.__den: int = denominator
# 		Fraction._count += 1
#
# 	@property
# 	def num(self) -> int:
# 		return self.__num
#
# 	@num.setter
# 	def num(self, value):
# 		if type(value) == int:
# 			self.__num = value
#
# 	def add(self, fraction: Fraction) -> Fraction:
# 		num = self.__num * fraction.__den + fraction.__num * self.__den
# 		den = self.__den * fraction.__den
# 		return Fraction(num, den)
#
# 	def multiply(self, fraction: Fraction) -> Fraction:
# 		num = self.__num * fraction.__num
# 		den = self.__den * fraction.__den
# 		return Fraction(num, den)
#
# 	def __str__(self) -> str:
# 		num = self.__num
# 		if self.__num > self.__den:
# 			int_part = int(self.__num / self.__den)
# 			num -= int_part * self.__den
# 			return f'{int_part} ({num}/{self.__den})'
# 		elif self.__num == self.__den:
# 			return str(int(self.__num / self.__den))
# 		return f'{self.__num}/{self.__den}'
#
# 	def __float__(self):
# 		return self.__num / self.__den
#
# 	@staticmethod
# 	def count_obj():
# 		return Fraction._count
#
#
#
# f1 = Fraction(2, 3, int_part=3)
# f2 = Fraction(3, 3)
#
# f3: Fraction = f1.add(f2)
# f4: Fraction = f3.add(f1)
# print(f2)
# print(Fraction.count_obj())
#

# Задание 2
# Создайте класс для конвертирования температуры из
# Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий. Также
# класс должен считать количество подсчетов температурыи
# возвращать это значение с помощью статического метода.


class Temperature:
	_count = 0

	def __init__(self, celsius: int, fahrenheit: int):
		self.celsius = celsius
		self.fahrenheit = fahrenheit
		Temperature._count += 1

	def celsius_to_fahrenheit(self):
		return self.celsius * (9 / 5) + 32

	def fahrenheit_to_celsius(self):
		return (self.fahrenheit - 32) * (5 / 9)

	def __str__(self):
		return f'Данная температура по Цельсию - {self.celsius} и данная температура по Фаренгейту {self.fahrenheit}'

	@staticmethod
	def count_obj():
		return Temperature._count


a1 = Temperature(20, 120)
print(f'Даны две температуры {a1}')
print(f'Температура в Цельсиях - {Temperature.fahrenheit_to_celsius(a1)} градусов')
print(f'Температура в Фаренгейтах - {Temperature.celsius_to_fahrenheit(a1)} градусов')


# Задание 3
# Создайте класс для перевода из метрической системы
# в английскую и наоборот. Функциональность необходимо
# реализовать в виде статических методов. Обязательно
# реализуйте перевод мер длины.

class Metric:

	def __init__(self, kilometres: int | float, miles:int | float):
		self.kilometres = kilometres
		self.miles = miles

	def kilometres_to_miles(self):
		self.miles = self.kilometres * 0,621371

	def miles_to_kilometres(self):
		self.kilometres = self.miles * 1,61

	def __str__(self):
		return f'Нам даны километры - {self.kilometres} и мили - {self.miles}'


a2 = Metric(250, 400)
print(f'Нам даны расстояния {a2}')
print(Metric.miles_to_kilometres(a2))
print(Metric.kilometres_to_miles(a2))
