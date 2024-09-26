# Задание 2
# Создайте класс Ship, который содержит информацию
# о корабле.
# С помощью механизма наследования, реализуйте
# класс Frigate (содержит информацию о фрегате), класс
# Destroyer (содержит информацию об эсминце), класс
# Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые
# для работы методы.


class Ship:

	def __init__(self, size: str, ship_type: str, country: str, sail_port: str):
		self._size = size
		self._ship_type = ship_type
		self._country = country
		self._sail_port = sail_port

	def __str__(self):
		return (f'Информация о корабле:'
						f' Размер корабля по водоизмещению - {self._size} '
						f' Тип корабля - {self._ship_type} '
						f' Страна производства корабля - {self._country} '
						f' Порт базирования  - {self._sail_port}')


class Frigate(Ship):

	def __init__(self, size: str, ship_type: str, country: str, sail_port: str, weapons: str):
		super().__init__(size, ship_type, country, sail_port)
		self._weapons = weapons

	def __str__(self):
		return super().__str__() + f' Тип вооружения - {self._weapons}'


class Destroyer(Ship):

	def __init__(self, size: str, ship_type: str, country: str, sail_port: str, atomic_weapons: str):
		super().__init__(size, ship_type, country, sail_port)
		self._atomic_weapons = atomic_weapons

	def __str__(self):
		return super().__str__() + f' Тип ядерного вооружения - {self._atomic_weapons}'


class Cruiser(Ship):

	def __init__(self, size: str, ship_type: str, country: str, sail_port: str, helicopter: str):
		super().__init__(size, ship_type, country, sail_port)
		self._helicopter = helicopter

	def __str__(self):
		return super().__str__() + f' Вертолеты на борту - {self._helicopter}'


a = Frigate('Среднее водоизмещение', 'Военный', 'Россия', 'Крым','ракеты земля-воздух')
b = Destroyer('Огромное водоизмещение', 'Военный', 'Россия', 'Владивосток', '20 боеголовок')
c = Cruiser('Малое водоизмещение','Военный','Россия','Мурманск','3 вертолета')
print(a)
print(b)
print(c)