# Задание 3
# Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
# В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, рубли и т.д.) и
# поле для хранения копеек (центы, евроценты, копейки
# и т.д.).
# Реализовать методы для вывода суммы на экран, задания значений для частей.
from __future__ import annotations
class Money:

	def __init__(self, dollars: int, euro: int, rubbles: int, cents: int, eurocents: int, coppecs: int):
		self._dollars = dollars
		self._euro = euro
		self._rubbles = rubbles
		self._cents = cents
		self._eurocents = eurocents
		self._coppecs = coppecs

	def input_money(self):
		self._dollars = int(input('Введите кол-во долларов - '))
		self._cents = self.validate_cents()
		self._euro = int(input('Введите кол-во евро - '))
		self._eurocents = self.validate_eurocents()
		self._rubbles = int(input('Введите кол-во рублей - '))
		self._coppecs = self.validate_coppecs()

	@staticmethod
	def validate_cents():
		while True:
			cents = int(input('Введите кол-во центов - '))
			if 0 <= cents < 100:
				return cents
			print('Число центов должно быть от 0 до 99')

	@staticmethod
	def validate_eurocents():
		while True:
			eurocents = int(input('Введите кол-во евроцентов - '))
			if 0 <= eurocents < 100:
				return eurocents
			print('Число евроцентов должно быть от 1 до 99')

	@staticmethod
	def validate_coppecs():
		while True:
			coppecs = int(input('Введите кол-во копеек - '))
			if 0 <= coppecs < 100:
				return coppecs
			print('Число копеек должно быть от 1 до 99')

	def __str__(self):
		return (f'У вас в кармане денег:'
		 f'Долларов - {self._dollars} и {self._cents} центов,'
		 f'Евро - {self._euro} и {self._eurocents} евроцентов,'
		 f'Рублей - {self._rubbles} и {self._coppecs} копеек)')


a = Money(1,1,1,1,1,1)
a.input_money()
print(a)
