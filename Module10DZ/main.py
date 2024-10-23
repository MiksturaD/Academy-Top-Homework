# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
import json


class Car:

	def __init__(self, brand: str, model: str, year:int, engine_capacity: float, color: str, price: int):
		self.brand: str = brand
		self.model = model
		self.year = year
		self.engine_capacity = engine_capacity
		self.color = color
		self.price = price


	def save(self):
		with open('cars.txt', 'a', encoding='utf-8') as f:
			f.write(f'{self.brand},{self.model},{self.year},{self.engine_capacity},{self.color},{self.price}\n')

	def to_json(self):
		with open('cars.json', 'w', encoding='utf-8') as f:
			json.dumps({self.brand},{self.model}, {self.year},{self.engine_capacity},{self.color},{self.price})

	def car_info(self):
		print(f'Название производителя - {self.brand}')
		print(f'Название модели - {self.model}')
		print(f'Год выпуска авто - {self.year}')
		print(f'Объем двигателя - {self.engine_capacity}')
		print(f'Цвет машины - {self.color}')
		print(f'Цена машины - {self.price} рублей')

	@staticmethod
	def open_file():
		with open('cars.txt', 'r', encoding='utf-8') as f:
			lines = f.readlines()
		return lines

	@staticmethod
	def show_brand():
		lines = Car.open_file()
		parts = lines[0].split(',')
		print(f'Название производителей в базе - {parts[0].strip()}')

	@staticmethod
	def model():
		lines = Car.open_file()
		parts = lines[0].split(',')
		print(f'Название моделей в базе - {parts[2].strip()}')

	@staticmethod
	def year():
		lines = Car.open_file()
		parts = lines[0].split(',')
		print(f'Год выпуска авто базе - {parts[3].strip()}')

	@staticmethod
	def engine():
		lines = Car.open_file()
		parts = lines[0].split(',')
		print(f'Объем двигателя в базе - {parts[4].strip()}')

	@staticmethod
	def color():
		lines = Car.open_file()
		parts = lines[0].split(',')
		print(f'Цвет авто в базе - {parts[5].strip()}')

	@staticmethod
	def price():
		lines = Car.open_file()
		parts = lines[0].split(',')
		print(f'Стоимость авто в базе - {parts[6].strip()}')


a = Car('Lexus', 'GS300h', '2018', '2500','white', '50000')
a.to_json()


# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.


# class Book:
#
# 	def __init__(self):
# 		with open('book.txt', 'r', encoding='utf-8') as f:
# 			# lines = f.readlines()
# 			self.name: str = input('Введите название книги: ')
# 			self.year = input('Введите год выпуска книги: ')
# 			self.publisher = input('Введите издателя: ')
# 			self.author = input('Введите автора: ')
# 			self.genre = input('Введите жанр: ')
# 			self.price = input('Введите стоимость книги: ')
#
# 	def save_book_info(self):
# 		with open('book.txt', 'a', encoding='utf-8') as f:
# 			f.write(f'{self.name},{self.year},{self.publisher},{self.author},{self.genre},{self.price}\n')
#
# 	@staticmethod
# 	def open_file():
# 		with open('book.txt', 'r', encoding='utf-8') as f:
# 			lines = f.readlines()
# 		return lines
#
# 	def show_book_info(self):
# 		print(f'Название книги - {self.name}')
# 		print(f'Год выпуска - {self.year}')
# 		print(f'Издатель - {self.publisher}')
# 		print(f'Автор - {self.author}')
# 		print(f'Жанр - {self.genre}')
# 		print(f'Цена - {self.price} рублей')
#
# 	@staticmethod
# 	def show_name():
# 		lines = Book.open_file()
# 		parts = lines[0].split(',')
# 		print(f'Название книг в базе - {parts[0].strip()}')
#
# 	@staticmethod
# 	def show_publisher():
# 		lines = Book.open_file()
# 		parts = lines[0].split(',')
# 		print(f'Название издателей в базе - {parts[3].strip()}')
#
# 	@staticmethod
# 	def show_year():
# 		lines = Book.open_file()
# 		parts = lines[0].split(',')
# 		print(f'Год выпуска книги в базе - {parts[2].strip()}')
#
# 	@staticmethod
# 	def show_author():
# 		lines = Book.open_file()
# 		parts = lines[0].split(',')
# 		print(f'Автор книги в базе - {parts[4].strip()}')
#
# 	@staticmethod
# 	def show_genre():
# 		lines = Book.open_file()
# 		parts = lines[0].split(',')
# 		print(f'Жанр книги в базе - {parts[5].strip()}')
#
# 	@staticmethod
# 	def show_price():
# 		lines = Book.open_file()
# 		parts = lines[0].split(',')
# 		print(f'Стоимость книги в базе - {parts[6].strip()}')
#
#
# a = Book()
# a.save_book_info()
# a.show_book_info()
# a.show_name()
# a.show_year()
# a.show_publisher()
# a.show_author()
# a.show_genre()
# a.show_price()


# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.


# class Stadium:
#
# 	def __init__(self):
# 		with open('stadium.txt', 'r', encoding='utf-8') as f:
# 			# lines = f.readlines()
# 			self.name: str = input('Введите название стадиона: ')
# 			self.year = input('Введите дату открытия стадиона: ')
# 			self.country = input('Введите страну: ')
# 			self.city = input('Введите город: ')
# 			self.capacity = input('Введите вместимость стадиона: ')
#
# 	def save_info(self):
# 		with open('stadium.txt', 'a', encoding='utf-8') as f:
# 			f.write(f'{self.name},{self.year},{self.country},{self.city},{self.capacity}\n')
#
# 	@staticmethod
# 	def open_file():
# 		with open('stadium.txt', 'r', encoding='utf-8') as f:
# 			lines = f.readlines()
# 		return lines
#
# 	def show_info(self):
# 		print(f'Название стадиона - {self.name}')
# 		print(f'Год постройки стадиона - {self.year}')
# 		print(f'Страна - {self.country}')
# 		print(f'Город - {self.city}')
# 		print(f'Вместимость - {self.capacity}')
#
# 	@staticmethod
# 	def show_name():
# 		lines = Stadium.open_file()
# 		parts = lines[0].split(',')
# 		print(f'Название стадиона в базе - {parts[0].strip()}')
#
# 	@staticmethod
# 	def show_country():
# 		lines = Stadium.open_file()
# 		parts = lines[0].split(',')
# 		print(f'Название страны в базе - {parts[2].strip()}')
#
# 	@staticmethod
# 	def show_year():
# 		lines = Stadium.open_file()
# 		parts = lines[0].split(',')
# 		print(f'Год постройки стадиона в базе - {parts[1].strip()}')
#
# 	@staticmethod
# 	def show_city():
# 		lines = Stadium.open_file()
# 		parts = lines[0].split(',')
# 		print(f'Город где стадион в базе - {parts[3].strip()}')
#
# 	@staticmethod
# 	def show_capacity():
# 		lines = Stadium.open_file()
# 		parts = lines[0].split(',')
# 		print(f'Вместимость стадиона в базе - {parts[4].strip()}')
#
#
# a = Stadium()
# a.save_info()
# a.show_name()
# a.show_year()
# a.show_country()
# a.show_city()
# a.show_capacity()
