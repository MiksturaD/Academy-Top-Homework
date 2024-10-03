# Задание 1
# Создайте функцию, возвращающую список со всеми
# простыми числами от 0 до 1000.
# Используя механизм декораторов посчитайте сколько
# секунд, потребовалось для вычисления всех простых чисел.
# Отобразите на экран количество секунд и простые числа.

# Задание 2
# Добавьте к первому заданию возможность передавать
# границы диапазона для поиска всех простых чисел.
#

import time


def time_worker(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time() - start
		print(f'Функция {func.__name__} выполнялась {end} с.')
		return result

	return wrapper


@time_worker
def simple_number(start: int, end: int):
	list = []
	for i in range(start, end):
		is_simple = True
		for j in range(2, int(i ** 0.5) + 1):  # Проверяем делимость на все числа от 2 до корня из i
			if i % j == 0:
				is_simple = False
				break
		if is_simple:
			list.append(i)
	return list


a = simple_number(0, 20000)
print(a)


# Задание 3
# Каждый год ваша компания предоставляет различным
# государственным организациям финансовую отчетность.
# В зависимости от организации форматы отчетности разные. Используя механизм декораторов, решите вопрос
# отчетности для организаций.

def tax_service(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		year_turn_over, expenses, staff = result
		tax_rate = 25  # Налоговая ставка для организации
		net_profit = year_turn_over - expenses
		tax = net_profit * (tax_rate / 100)
		return (f'Чистая прибыль компании равна - {net_profit - tax}$'
						f' Налоги к оплате - {tax}$')
	return wrapper


def labor_inspection(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		year_turn_over, expenses, staff = result
		wage_fond = expenses * 0.5  # Фонд оплаты труда
		deductions = wage_fond * 0.25  # Отчисления в ПФР и страховые
		return (f'Фонд заработной платы для - {staff} сотрудников равен - {wage_fond}$'
						f' отчисления в ПФР и страховые взносы составили - {deductions}$')
	return wrapper


def company_of_dust(year_turn_over: float, expenses: float, staff: int):
	return year_turn_over, expenses, staff


a = tax_service(company_of_dust)
b = labor_inspection(company_of_dust)


print(a(250000, 125000, 44))
print(b(250000, 125000, 44))
