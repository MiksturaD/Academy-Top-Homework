# Задание 1
# Создайте класс Device, который содержит информацию об устройстве.
# С помощью механизма наследования, реализуйте класс
# CoffeeMachine (Содержит информацию о кофемашине)
# класс Blender (содержит информацию о блендере), класс
# MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые
# для работы методы.


class Device:
	def __init__(self, type_device: str, size: str, power: str):
		self._type_device = type_device
		self._size = size
		self._power = power

	def __str__(self):
		return (f'Информация о устройстве: тип устройства - {self._type_device},'
						f' Размер устройства - {self._size},'
						f' Мощность устройства - {self._power},')


class CoffeeMachine(Device):

	def __init__(self, type_device: str, size: str, power: str, type_coffee_machine: str):
		super().__init__(type_device, size, power)
		self._type_coffee_machine = type_coffee_machine

	def __str__(self):
		return super().__str__() + f'Тип кофемашины - {self._type_coffee_machine}'


class Blender(Device):

	def __init__(self, type_device: str, size: str, power: str, type_blender: str):
		super().__init__(type_device, size, power)
		self._type_blender = type_blender

	def __str__(self):
		return super().__str__() + f'Тип блендера - {self._type_blender}'


class MeatGrinder(Device):

	def __init__(self, type_device: str, size: str, power: str, type_meat_grinder: str):
		super().__init__(type_device, size, power)
		self._type_meat_grinder = type_meat_grinder

	def __str__(self):
		return super().__str__() + f'Тип мясорубки - {self._type_meat_grinder}'


a = CoffeeMachine('Кофеварка', 'Маленькая', '1200w', 'Рожковая-профессиональная')
b = Blender('Блендер кухонный', 'Небольшой', '500w', 'Погружной')
c = MeatGrinder('Мясорубка', 'Огромная', '5000w', 'Уничтожитель плоти')

print(a)
print(b)
print(c)