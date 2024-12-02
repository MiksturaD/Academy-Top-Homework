import json
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import telebot

from telebot import types
from list import token

# Создаем экземпляр бота
bot = telebot.TeleBot(token)

# Список для хранения привычек
habits = []

# Настройка подключения к базе данных (например, SQLite)
engine = create_engine('sqlite:///habits.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

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


class Habit(Base):
    __tablename__ = 'habits'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    target_date = Column(DateTime)

    Base.metadata.create_all(engine)

    def __repr__(self):
        return f'Название: {self.name}\nОписание: {self.description}\nЦелевая дата: {self.target_date}'

    def save(self, habits: list):
        habits.append(self)

    @staticmethod
    def create_habit(message):
        habit_name = message.text
        new_habit = Habit(name=habit_name)
        session.add(new_habit)
        session.commit()
        bot.send_message(message.chat.id, f'Привычка "{habit_name}" успешно создана!')
        bot.send_message(message.chat.id, 'Введите описание привычки:')
        bot.register_next_step_handler(message, Habit.create_habit_description)

    @staticmethod
    def create_habit_description(message):
        habit_description = message.text
        habit = session.query(Habit).order_by(Habit.id.desc()).first()
        habit.description = habit_description
        session.commit()
        bot.send_message(message.chat.id, 'Теперь введите целевую дату выполнения привычки в формате дд.мм.гггг:')
        bot.register_next_step_handler(message, Habit.create_habit_target_date)

    @staticmethod
    def create_habit_target_date(message):
        try:
            target_date = datetime.strptime(message.text, '%d.%m.%Y')
            habit = session.query(Habit).order_by(Habit.id.desc()).first()
            habit.target_date = target_date
            session.commit()
            bot.send_message(message.chat.id, 'Привычка успешно создана!')
        except ValueError:
            bot.send_message(message.chat.id, 'Пожалуйста, введите дату в формате ДД.ММ.ГГГГ.')
            bot.register_next_step_handler(message, Habit.create_habit_target_date)

    @staticmethod
    def view_habits(message):
        habits = session.query(Habit).all()
        habits_str = '\n\n'.join(str(habit) for habit in habits)
        bot.send_message(message.chat.id, f'Ваши привычки:\n\n{habits_str}')

    @staticmethod
    def delete_habit(message):
        habit_name = message.text
        habit = session.query(Habit).filter_by(name=habit_name).first()
        if habit:
            session.delete(habit)
            session.commit()
            bot.send_message(message.chat.id, 'Привычка успешно удалена!')
        else:
            bot.send_message(message.chat.id, 'Привычка с таким названием не найдена.')


# Запускаем бота
bot.polling(none_stop=True, interval=0)