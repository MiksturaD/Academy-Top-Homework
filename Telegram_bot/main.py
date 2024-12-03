from datetime import datetime
import telebot
from telebot import types
from list import token
import sys
import os
from bot.database import init_db, add_habit, get_habits, delete_habit, add_habit_progress, get_habit_progress
from bot.utils import Habit
# Создаем экземпляр бота
bot = telebot.TeleBot(token)

# Инициализация базы данных
init_db()


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



@bot.message_handler(content_types=["text"])
def handle_text(message, create_habit=None):
    # Если юзер прислал 1, создаем новую привычку
    if message.text.strip() == 'Создание привычки':
        bot.send_message(message.chat.id, 'Введите название привычки:')
        bot.register_next_step_handler(message, Habit_bot.create_habit_name)
    # Если юзер прислал 2, выдаем список привычек
    elif message.text.strip() == 'Список привычек':
        Habit_bot.view_habits(message)  # Вызов метода view_habits с передачей сообщения
    elif message.text.strip() == 'Удаление привычки':
        bot.send_message(message.chat.id, 'Введите название привычки для удаления:')
        bot.register_next_step_handler(message, Habit_bot.delete_habit_name)
    elif message.text.strip() == 'Выполнение привычки':
        bot.send_message(message.chat.id, 'Здесь будем выполнять действие по привычке')
        bot.register_next_step_handler(message, Habit_bot.execute_habit_name)


class Habit_bot:

    def __init__(self, name: str, description: str = None, target_date: str = None) -> None:
        self.name = name
        self.description = description
        self.target_date = target_date


    def __repr__(self) -> str:
        return f'Название: {self.name}\nОписание: {self.description}\nЦелевая дата: {self.target_date}'


    @staticmethod
    def view_habits(message):
        """Отображение списка привычек."""
        habits = get_habits()
        if habits:
            habits_str = '\n\n'.join(
                [str(Habit(habit['name'], habit['description'], habit['target_date'])) for habit in habits])
            bot.send_message(message.chat.id, f'Ваши привычки:\n\n{habits_str}')
        else:
            bot.send_message(message.chat.id, 'У вас нет привычек.')


    @staticmethod
    def delete_habit_name(message):
        """Обработчик ввода названия привычки для удаления."""
        habit_name = message.text
        if delete_habit(habit_name):
            bot.send_message(message.chat.id, f'Привычка "{habit_name}" успешно удалена!')
        else:
            bot.send_message(message.chat.id, f'Привычка с названием "{habit_name}" не найдена.')

    @staticmethod
    def create_habit_name(message):
        """Обработчик ввода названия привычки."""
        bot.send_message(message.chat.id, 'Введите описание привычки:')
        bot.register_next_step_handler(message, Habit_bot.create_habit_description, habit_name=message.text)


    @staticmethod
    def create_habit_description(message, habit_name: str):
        """Обработчик ввода описания привычки."""
        bot.send_message(message.chat.id, 'Введите целевую дату выполнения привычки в формате ДД.ММ.ГГГГ:')
        bot.register_next_step_handler(message, Habit_bot.create_habit_target_date, habit_name=habit_name,
                                            habit_description=message.text)


    @staticmethod
    def create_habit_target_date(message, habit_name: str, habit_description: str):
        """Обработчик ввода целевой даты привычки."""
        try:
            target_date = message.text
            habit = Habit(name=habit_name, description=habit_description, target_date=target_date)
            add_habit(habit.name, habit.description, habit.target_date)
            bot.send_message(message.chat.id, f'Привычка "{habit.name}" успешно создана!')
        except ValueError:
            bot.send_message(message.chat.id, 'Пожалуйста, введите дату в формате ДД.ММ.ГГГГ.')
            bot.register_next_step_handler(message, Habit_bot.create_habit_target_date, habit_name=habit_name,
                                           habit_description=habit_description)

    @staticmethod
    def execute_habit_name(message):
        """Обработчик ввода названия привычки для выполнения."""
        habit_name = message.text
        habits = get_habits()
        habit = next((h for h in habits if h['name'] == habit_name), None)
        if habit:
            bot.send_message(message.chat.id, 'Введите прогресс выполнения привычки:')
            bot.register_next_step_handler(message, Habit_bot.execute_habit_progress, habit_id=habit['id'])
        else:
            bot.send_message(message.chat.id, f'Привычка с названием "{habit_name}" не найдена.')

    @staticmethod
    def execute_habit_progress(message, habit_id: int):
        """Обработчик ввода прогресса выполнения привычки."""
        progress = message.text
        progress_date = datetime.now().strftime('%d.%m.%Y')
        add_habit_progress(habit_id, progress_date, progress)
        bot.send_message(message.chat.id, f'Прогресс выполнения привычки успешно сохранен!')

# Запускаем бота
bot.polling(none_stop=True, interval=0)