# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.


class Car:


	def __init__(self):
		with open('cars.txt', 'r', encoding='utf-8') as f:
			# lines = f.readlines()
			self.brand: str = input('Введите название производителя: ')
			self.model = input('Введите название модели: ')
			self.year = input('Введите год выпуска авто: ')
			self.engine_capacity = input('Введите объем двигателя: ')
			self.color = input('Введите цвет машины: ')
			self.price = input('Введите стоимость машины: ')

	def save_cars_info(self):
		with open('cars.txt', 'a', encoding='utf-8') as f:
			f.write(f'{self.brand},{self.model},{self.year},{self.engine_capacity},{self.color},{self.price}\n')


	def show_car_info(self):
		print(f'Название производителя - {self.brand}')
		print(f'Название модели - {self.model}')
		print(f'Год выпуска авто - {self.year}')
		print(f'Объем двигателя - {self.engine_capacity}')
		print(f'Цвет машины - {self.color}')
		print(f'Цена машины - {self.price} рублей')

	def show_brand(self):
		with open('cars.txt', 'r', encoding='utf-8') as f:
			lines = f.readlines()
			for line in lines:
				parts = line.split(',')
				print(f'Название производителей в базе - {parts[0].strip()}')


	def show_model(self):
		with open('cars.txt', 'r', encoding='utf-8') as f:
			lines = f.readlines()
			for line in lines:
				parts = line.split(',')
				print(f'Название моделей в базе - {parts[2].strip()}')


	def show_year(self):
		with open('cars.txt', 'r', encoding='utf-8') as f:
			lines = f.readlines()
			for line in lines:
				parts = line.split(',')
				print(f'Год выпуска авто базе - {parts[3].strip()}')


	def show_engine(self):
		with open('cars.txt', 'r', encoding='utf-8') as f:
			lines = f.readlines()
			for line in lines:
				parts = line.split(',')
				print(f'Объем двигателя в базе - {parts[4].strip()}')


	def show_color(self):
		with open('cars.txt', 'r', encoding='utf-8') as f:
			lines = f.readlines()
			for line in lines:
				parts = line.split(',')
				print(f'Цвет авто в базе - {parts[5].strip()}')


	def show_price(self):
		with open('cars.txt', 'r', encoding='utf-8') as f:
			lines = f.readlines()
			for line in lines:
				parts = line.split(',')
				print(f'Стоимость авто в базе - {parts[6].strip()}')

a = Car()
a.save_cars_info()
a.show_car_info()
a.show_brand()


