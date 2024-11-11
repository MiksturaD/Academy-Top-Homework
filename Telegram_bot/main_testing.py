import json
from datetime import datetime

import telebot

from telebot import types
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



@bot.message_handler(content_types=["text"])
def handle_text(message, create_habit=None):
    # Если юзер прислал 1, создаем новую привычку
    if message.text.strip() == 'Создание привычки':
        bot.send_message(message.chat.id, 'Введите название привычки:')
        bot.register_next_step_handler(message, Habit.create_habit)
    # Если юзер прислал 2, выдаем список привычек
    elif message.text.strip() == 'Список привычек':
        bot.send_message(message.chat.id, Habit.view_habits)
    elif message.text.strip() == 'Удаление привычки':
        bot.send_message(message.chat.id, 'Введите название привычки для удаления:')
        bot.register_next_step_handler(message, Habit.delete_habit)
    elif message.text.strip() == 'Выполнение привычки':
        bot.send_message(message.chat.id, 'Здесь будем выполнять действие по привычке')


class Habit:
    def __init__(self, name: str, description: str = None, target_date: str = None) -> None:
        self.name = name
        self.description = description
        self.target_date = target_date


    def __repr__(self) -> str:
        return f'Название: {self.name}\nОписание: {self.description}\nЦелевая дата: {self.target_date}'

    def save(self, habits: list):
        habits.append(self)

    @staticmethod
    def view_habits(message) -> None:
        try:
            with open('habits.json', 'r', encoding='utf-8') as f:
                loaded_json = json.load(f)

            habits = []
            for habit_data in loaded_json:
                habit = Habit(name=habit_data['name'], description=habit_data.get('description'),
                              target_date=habit_data['target_date'])
                habits.append(str(habit))

            habits_str = '\n\n'.join(habits)
            bot.send_message(message.chat.id, f'Ваши привычки:\n\n{habits_str}')
        except FileNotFoundError:
            bot.send_message(message.chat.id, 'Файл с привычками не найден.')
        except json.JSONDecodeError:
            bot.send_message(message.chat.id, 'Произошла ошибка при чтении файла.')

    @staticmethod
    def delete_habit(message):
        try:
            with open('habits.txt', 'r', encoding='utf-8') as f:
                lines = f.readlines()

            with open('habits.txt', 'w', encoding='utf-8') as f:
                deleted = False
                for line in lines:
                    habit_data = line.strip().split(',')
                    print(f"Проверяемая строка: {line.strip()}")  # Отладочная информация
                    if message == habit_data[0].strip():
                        print(f"Удаляемая строка: {line.strip()}")  # Отладочная информация
                        deleted = True
                    else:
                        f.write(line)
                if deleted:
                    bot.send_message(message.chat.id, 'Привычка успешно удалена!')
                else:
                    bot.send_message(message.chat.id, 'Привычка с таким названием не найдена.')
        except FileNotFoundError:
            bot.send_message(message.chat.id, 'Файл с привычками не найден.')
        except IOError:
            bot.send_message(message.chat.id, 'Произошла ошибка при чтении файла.')

    @staticmethod
    def create_habit(message):
        habit_name = message.text
        habits.append({'name': habit_name,
                       'description': '',
                       'target_date': None
                       })
        bot.send_message(message.chat.id,
                         f'Привычка "{habit_name}" успешно создана! Теперь вы можете добавить описание или целевую дату.')
        bot.send_message(message.chat.id, 'Введите описание привычки:')
        bot.register_next_step_handler(message, Habit.create_habit_description)

    @staticmethod
    def create_habit_description(message):
        habit_description = message.text
        habits[-1]['description'] = habit_description
        bot.send_message(message.chat.id, 'Теперь введите целевую дату выполнения привычки в формате дд.мм.гггг:')
        bot.register_next_step_handler(message, Habit.create_habit_target_date)

    @staticmethod
    def _datetime_to_json(obj):
        if isinstance(obj, datetime):
            return obj.strftime('%d.%m.%Y')
        raise TypeError(f'Object of type {obj.__class__.__name__} '
                        f'is not JSON serializable')

    @staticmethod
    def create_habit_target_date(message):
        try:
            target_date = datetime.strptime(message.text, '%d.%m.%Y')
            habit = {'name': habits[-1]['name'], 'description': habits[-1]['description'], 'target_date': target_date}
            habits[-1] = habit
            with open('habits.json', 'a', encoding='utf-8') as f:
                json.dump(habits, f,  ensure_ascii=False, default=Habit._datetime_to_json)
            bot.send_message(message.chat.id, 'Привычка успешно создана!')
        except ValueError:
            bot.send_message(message.chat.id, 'Пожалуйста, введите дату в формате ДД.ММ.ГГГГ.')
            bot.register_next_step_handler(message, Habit.create_habit_target_date)


# Запускаем бота
bot.polling(none_stop=True, interval=0)