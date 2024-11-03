from telebot import types

# Классы по созданию привычек
class Habit:

	def __init__(self, name: str, target: int = 0) -> None:
		self._name: str = name
		self._target: int = target

	def save(self, habits: list):
		habits.append(self)

