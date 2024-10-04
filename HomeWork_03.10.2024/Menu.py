from typing import Callable


class Menu:
	def __init__(self):
		self.__items: dict = {}

	def add_item(self, name: str, func: Callable, **kwargs):
		key = len(self.__items.keys()) + 1
		self.__items[key] = {
			'name': name,
			'call': func,
			'kwargs': kwargs
		}

	def choose(self):
		c = int(input('Введите пункт меню: '))
		if 1 <= c <= len(self.__items.keys()):
			args = Menu.get_kwargs_from_console(self.__items[c]['kwargs'])
			self.__items[c]['call'](*args)

	@staticmethod
	def get_kwargs_from_console(kwargs):
		args = []
		for key in kwargs.keys():
			args.append(input(f'Введите {key}: '))
		return args

	def print(self):
		for i, value in self.__items.items():
			print(f'{i}. {value["name"]}')
