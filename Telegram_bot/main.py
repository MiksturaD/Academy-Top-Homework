from datetime import datetime

import telebot
import random

import json
from telebot import types
from habit import Habit
from list import token

# Создаем экземпляр бота
bot = telebot.TeleBot(token)

# Список для хранения привычек
habits = []


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
	# Добавляем 4 кнопки
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Создание привычки")
	item2 = types.KeyboardButton("Список привычек")
	item3 = types.KeyboardButton("Удаление привычки")
	item4 = types.KeyboardButton("Выполнение привычки")
	markup.add(item1)
	markup.add(item2)
	markup.add(item3)
	markup.add(item4)
	bot.send_message(m.chat.id, 'Нажми:'
															'\nСоздание привычки - для создания новой привычки'
															'\nСписок привычек - для просмотра существующих привычек'
															'\nУдаление привычки - для удаления ненужной привычки'
															'\nВыполнение привычки - для успешного выполнения той или иной привычки',
									 reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
	# Если юзер прислал 1, создаем новую привычку
	if message.text.strip() == 'Создание привычки':
		bot.send_message(message.chat.id, 'Введите название привычки:')
		bot.register_next_step_handler(message, create_habit)
	# Если юзер прислал 2, выдаем список привычек
	elif message.text.strip() == 'Список привычек':
		bot.send_message(message.chat.id, view_habits(message))
	elif message.text.strip() == 'Удаление привычки':
		bot.send_message(message.chat.id, 'Введите название привычки для удаления:')
		bot.register_next_step_handler(message, delete_habit)
	elif message.text.strip() == 'Выполнение привычки':
		bot.send_message(message.chat.id, 'Здесь будем выполнять действие по привычке')


def view_habits(message):
	habits = []
	with open('habits.txt', 'r', encoding='utf-8') as f:
		for line in f:
			habit_data = line.strip().split(',')
			habit = {
				'name': habit_data[0],
				'description': habit_data[1],
				'target_date': habit_data[2]
			}
			habits.append(habit)
	habits_str = '\n'.join([
		f'Название: {habit["name"]}\nОписание: {habit["description"]}\nЦелевая дата: {habit["target_date"]}'
		for habit in habits
	])
	return f'Ваши привычки:\n{habits_str}'


def delete_habit(message):
	with open('habits.txt', 'r', encoding='utf-8') as f:
		for line in f:
			habit_data = line.strip().split(',')
			habit = {
				'name': habit_data[0],
				'description': habit_data[1],
				'target_date': habit_data[2]
			}
			habits.append(habit)

	with open('habits.txt', 'w', encoding='utf-8') as f:
		for habit in habits:
			if message == habit_data[0]:
				f.write(line)
	bot.send_message(message.chat.id, 'Привычка успешно удалена!')


def create_habit(message):
	habit_name = message.text
	habits.append({'name': habit_name, 'description': '', 'target_date': None})
	bot.send_message(message.chat.id,
									 f'Привычка "{habit_name}" успешно создана! Теперь вы можете добавить описание или целевую дату.')
	bot.send_message(message.chat.id, 'Введите описание привычки:')
	bot.register_next_step_handler(message, create_habit_description)


def create_habit_description(message):
	habit_description = message.text
	habits[-1]['description'] = habit_description
	bot.send_message(message.chat.id, 'Теперь введите целевую дату выполнения привычки в формате дд.мм.гггг:')
	bot.register_next_step_handler(message, create_habit_target_date)


class CustomJSONEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, datetime):
			return obj.strftime('%d.%m.%Y')
		return super().default(obj)


def create_habit_target_date(message):
	try:
		target_date = datetime.strptime(message.text, '%d.%m.%Y')
		habit = {'name': habits[-1]['name'], 'description': habits[-1]['description'], 'target_date': target_date}
		habits[-1] = habit
		habit_str = f"Название: {habit['name']},Описание: {habit['description']},Целевая дата: {habit['target_date']}"
		with open('habits.txt', 'a', encoding='utf-8') as f:
			f.write(habit_str + '\n')  # Записываем каждую привычку на новой строке
		bot.send_message(message.chat.id, 'Привычка успешно создана!')
	except ValueError:
		bot.send_message(message.chat.id, 'Пожалуйста, введите дату в формате ДД.ММ.ГГГГ.')
		bot.register_next_step_handler(message, create_habit_target_date)


# Запускаем бота
bot.polling(none_stop=True, interval=0)
