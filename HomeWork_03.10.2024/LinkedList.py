from __future__ import annotations


class Item:
	def __init__(self, value: int, nxt: Item | None = None):
		self.value: int = value
		self.next: Item = nxt

	def __str__(self) -> str:
		return f'[{self.value} | {self.next}]'


class LinkedList:
	def __init__(self):
		self.__start: Item | None = None
		self.__current: Item | None = None
		self.__last: Item | None = None

	def add(self, value: int):
		if self.__start is None:
			item: Item = Item(value)
			self.__start = item
			self.__current = item
			self.__last = item
		else:
			item: Item = Item(value)
			self.__last.next = item
			self.__last = item

	def remove(self):
		current = self.__start
		while current.next != self.__last:
			current = current.next
		current.next = None

	def get(self):
		if self.__current is None:
			raise Exception('Конец, больше нет элементов в списке')

		return self.__current.value

	def update(self, value: int):
		self.__current.value = value

	def show(self):
		print(self.__current)

	def next(self):
		self.__current = self.__current.next