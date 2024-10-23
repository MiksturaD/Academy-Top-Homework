# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
import json
import pickle
from ctypes import c_char


class Car:

	def __init__(self, brand: str, model: str, year:int, engine_capacity: float, color: str, price: int)-> None:
		self.brand: str = brand
		self.model: str = model
		self.year: int = year
		self.engine_capacity: float = engine_capacity
		self.color: str = color
		self.price: int = price


	def save(self) -> None:
		with open('cars.txt', 'a', encoding='utf-8') as f:
			f.write(f'{self.brand},{self.model},{self.year},{self.engine_capacity},{self.color},{self.price}\n')

	def to_json(self)-> None:
		car_dict = {
			'brand': self.brand,
			'model': self.model,
			'year': self.year,
			'engine_capacity': self.engine_capacity,
			'color': self.color,
			'price': self.price
		}
		with open('cars.json', 'w', encoding='utf-8') as f:
			json.dump(car_dict, f, ensure_ascii=False)

	@staticmethod
	def from_json()-> None:
		with open('cars.json', 'r', encoding='utf-8') as f:
			loaded_json = json.load(f)

	def to_pickle(self)-> None:
		car_dict = {
			'brand': self.brand,
			'model': self.model,
			'year': self.year,
			'engine_capacity': self.engine_capacity,
			'color': self.color,
			'price': self.price
		}
		with open('cars.pickle', 'wb') as f:
			pickle.dump(car_dict, f)


	@staticmethod
	def from_pickle()-> None:
		with open('cars.pickle', 'rb') as f:
			loaded_pickle = pickle.load(f)

	def car_info(self)-> None:
		print(f'Название производителя - {self.brand}')
		print(f'Название модели - {self.model}')
		print(f'Год выпуска авто - {self.year}')
		print(f'Объем двигателя - {self.engine_capacity}')
		print(f'Цвет машины - {self.color}')
		print(f'Цена машины - {self.price} рублей')

	@staticmethod
	def open_file()-> list:
		with open('cars.txt', 'r', encoding='utf-8') as f:
			lines = f.readlines()
		return lines

	@staticmethod
	def show_brand()-> None:
		lines = Car.open_file()
		parts = lines[0].split(',')
		print(f'Название производителей в базе - {parts[0].strip()}')

	@staticmethod
	def model()-> None:
		lines = Car.open_file()
		parts = lines[0].split(',')
		print(f'Название моделей в базе - {parts[2].strip()}')

	@staticmethod
	def year()-> None:
		lines = Car.open_file()
		parts = lines[0].split(',')
		print(f'Год выпуска авто базе - {parts[3].strip()}')

	@staticmethod
	def engine()-> None:
		lines = Car.open_file()
		parts = lines[0].split(',')
		print(f'Объем двигателя в базе - {parts[4].strip()}')

	@staticmethod
	def color()-> None:
		lines = Car.open_file()
		parts = lines[0].split(',')
		print(f'Цвет авто в базе - {parts[5].strip()}')

	@staticmethod
	def price()-> None:
		lines = Car.open_file()
		parts = lines[0].split(',')
		print(f'Стоимость авто в базе - {parts[6].strip()}')


a = Car('Lexus', 'GS300h', '2018', '2500','white', '50000')
a.to_json()
a.from_json()
a.to_pickle()



# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.


class Book:

	def __init__(self, name: str, year: int, publisher: str, author: str, genre: str, price: int):
		self.name: str = name
		self.year: int = year
		self.publisher: str = publisher
		self.author: str = author
		self.genre: str = genre
		self.price: int = price


	def save_book_info(self):
		with open('book.txt', 'a', encoding='utf-8') as f:
			f.write(f'{self.name},{self.year},{self.publisher},{self.author},{self.genre},{self.price}\n')

	def to_json(self)-> None:
		book_dict = {
			'name': self.name,
			'year': self.year,
			'publisher': self.publisher,
			'author': self.author,
			'genre': self.genre,
			'price': self.price
		}
		with open('books.json', 'w', encoding='utf-8') as f:
			json.dump(book_dict, f, ensure_ascii=False)

	@staticmethod
	def from_json()-> None:
		with open('books.json', 'r', encoding='utf-8') as f:
			loaded_json = json.load(f)

	def to_pickle(self)-> None:
		book_dict = {
			'name': self.name,
			'year': self.year,
			'publisher': self.publisher,
			'author': self.author,
			'genre': self.genre,
			'price': self.price
		}
		with open('books.pickle', 'wb') as f:
			pickle.dump(book_dict, f)


	@staticmethod
	def from_pickle()-> None:
		with open('books.pickle', 'rb') as f:
			loaded_pickle = pickle.load(f)

	@staticmethod
	def open_file():
		with open('book.txt', 'r', encoding='utf-8') as f:
			lines = f.readlines()
		return lines

	def show_book_info(self):
		print(f'Название книги - {self.name}')
		print(f'Год выпуска - {self.year}')
		print(f'Издатель - {self.publisher}')
		print(f'Автор - {self.author}')
		print(f'Жанр - {self.genre}')
		print(f'Цена - {self.price} рублей')

	@staticmethod
	def show_name():
		lines = Book.open_file()
		parts = lines[0].split(',')
		print(f'Название книг в базе - {parts[0].strip()}')

	@staticmethod
	def show_publisher():
		lines = Book.open_file()
		parts = lines[0].split(',')
		print(f'Название издателей в базе - {parts[3].strip()}')

	@staticmethod
	def show_year():
		lines = Book.open_file()
		parts = lines[0].split(',')
		print(f'Год выпуска книги в базе - {parts[2].strip()}')

	@staticmethod
	def show_author():
		lines = Book.open_file()
		parts = lines[0].split(',')
		print(f'Автор книги в базе - {parts[4].strip()}')

	@staticmethod
	def show_genre():
		lines = Book.open_file()
		parts = lines[0].split(',')
		print(f'Жанр книги в базе - {parts[5].strip()}')

	@staticmethod
	def show_price():
		lines = Book.open_file()
		parts = lines[0].split(',')
		print(f'Стоимость книги в базе - {parts[6].strip()}')


b = Book('Сварог', '2005', 'ЭКМО', 'А.Бушков', 'Фэнтази', 100)
b.to_json()
b.to_pickle()
b.from_json()
b.from_pickle()



# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.


class Stadium:

	def __init__(self, name: str, year: int, country: str, city: str, capacity: int):
		self.name: str = name
		self.year: int = year
		self.country: str = country
		self.city: str = city
		self.capacity: int = capacity

	def save_info(self):
		with open('stadium.txt', 'a', encoding='utf-8') as f:
			f.write(f'{self.name},{self.year},{self.country},{self.city},{self.capacity}\n')

	def to_json(self)-> None:
		stadium_dict = {
			'name': self.name,
			'year': self.year,
			'country': self.country,
			'city': self.city,
			'capacity': self.capacity
		}
		with open('stadium.json', 'w', encoding='utf-8') as f:
			json.dump(stadium_dict, f, ensure_ascii=False)

	@staticmethod
	def from_json()-> None:
		with open('stadium.json', 'r', encoding='utf-8') as f:
			loaded_json = json.load(f)

	def to_pickle(self)-> None:
		stadium_dict = {
			'name': self.name,
			'year': self.year,
			'country': self.country,
			'city': self.city,
			'capacity': self.capacity
		}
		with open('stadium.pickle', 'wb') as f:
			pickle.dump(stadium_dict, f)

	@staticmethod
	def from_pickle()-> None:
		with open('stadium.pickle', 'rb') as f:
			loaded_pickle = pickle.load(f)

	@staticmethod
	def open_file():
		with open('stadium.txt', 'r', encoding='utf-8') as f:
			lines = f.readlines()
		return lines

	def show_info(self):
		print(f'Название стадиона - {self.name}')
		print(f'Год постройки стадиона - {self.year}')
		print(f'Страна - {self.country}')
		print(f'Город - {self.city}')
		print(f'Вместимость - {self.capacity}')

	@staticmethod
	def show_name():
		lines = Stadium.open_file()
		parts = lines[0].split(',')
		print(f'Название стадиона в базе - {parts[0].strip()}')

	@staticmethod
	def show_country():
		lines = Stadium.open_file()
		parts = lines[0].split(',')
		print(f'Название страны в базе - {parts[2].strip()}')

	@staticmethod
	def show_year():
		lines = Stadium.open_file()
		parts = lines[0].split(',')
		print(f'Год постройки стадиона в базе - {parts[1].strip()}')

	@staticmethod
	def show_city():
		lines = Stadium.open_file()
		parts = lines[0].split(',')
		print(f'Город где стадион в базе - {parts[3].strip()}')

	@staticmethod
	def show_capacity():
		lines = Stadium.open_file()
		parts = lines[0].split(',')
		print(f'Вместимость стадиона в базе - {parts[4].strip()}')


c = Stadium('Центральный', 1970, 'Russia', 'Krasnoyarsk', 20000)
c.to_json()
c.from_json()
c.to_pickle()
c.from_pickle()
