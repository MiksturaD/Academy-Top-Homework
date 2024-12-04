from datetime import datetime
import telebot
from telebot import types
from list import token

from bot.database import init_db, add_habit, get_habits, delete_habit, add_habit_progress, get_habit_progress
from bot.utils import Habit

# Создаем экземпляр бота
bot = telebot.TeleBot(token)

# Инициализация базы данных
init_db()


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Добавляем 5 кнопок
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Создание привычки")
    item2 = types.KeyboardButton("Список привычек")
    item3 = types.KeyboardButton("Удаление привычки")
    item4 = types.KeyboardButton("Выполнение привычки")
    item5 = types.KeyboardButton("Показать текущий прогресс выполнение привычки")
    item6 = types.KeyboardButton("Написать автору")

    markup.add(item1, item2)
    markup.add(item3, item4)
    markup.add(item5, item6)

    bot.send_message(m.chat.id, 'Нажми:'
                                '\nСоздание привычки - для создания новой привычки'
                                '\nСписок привычек - для просмотра существующих привычек'
                                '\nУдаление привычки - для удаления ненужной привычки'
                                '\nВыполнение привычки - для успешного выполнения той или иной привычки'
                                '\nПоказать текущий прогресс выполнения привычки - для просмотра прогресса выполнения привычки',
                     reply_markup=markup)



@bot.message_handler(content_types=["text"])
def handle_text(message, create_habit=None):
    habit_id = 0
    # Если юзер прислал 1, создаем новую привычку
    if message.text.strip() == 'Создание привычки':
        bot.send_message(message.chat.id, 'Введите название привычки:')
        bot.register_next_step_handler(message, Habit_bot.create_habit_name)
    # Если юзер прислал 2, выдаем список привычек
    elif message.text.strip() == 'Список привычек':
        Habit_bot.view_habits(message)  # Вызов метода view_habits с передачей сообщения
    elif message.text.strip() == 'Удаление привычки':
        bot.send_message(message.chat.id, 'Введите ID привычки для удаления:')
        bot.register_next_step_handler(message, Habit_bot.delete_habit_name)
    elif message.text.strip() == 'Выполнение привычки':
        bot.send_message(message.chat.id, 'Введите ID привычки, которую хотите выполнить:')
        bot.register_next_step_handler(message, Habit_bot.execute_habit_name)
    elif message.text.strip() == 'Показать текущий прогресс выполнение привычки':
        bot.send_message(message.chat.id, 'Введите ID привычки, которую хотите посмотреть:')
        bot.register_next_step_handler(message, Habit_bot.view_habit_progress_id)



class Habit_bot:

    def __init__(self, name: str, description: str = None, metric: str = None, target_date: str = None) -> None:
        self.name = name
        self.description = description
        self.metric = metric
        self.target_date = target_date



    def __repr__(self) -> str:
        return (f'Название: {self.name}\nОписание: {self.description}\nЕдиница измерения: {self.metric}\n'
                f'Целевая дата: {self.target_date}')

    @staticmethod
    def view_habits(message):
        """Отображение списка привычек."""
        user_id = message.from_user.id
        habits = get_habits(user_id)
        if habits:
            habits_str = '\n\n'.join(
                [f'ID: {habit["id"]}\nНазвание: {habit["name"]}\nОписание: {habit["description"]}\n'
                 f'Единица измерения: {habit["metric"]}\nЦелевая дата: {habit["target_date"]}' for habit in habits])
            bot.send_message(message.chat.id, f'Ваши привычки:\n\n{habits_str}')
        else:
            bot.send_message(message.chat.id, 'У вас нет привычек.')

    @staticmethod
    def delete_habit_name(message):
        """Обработчик ввода ID привычки для удаления."""
        user_id = message.from_user.id
        try:
            habit_id = int(message.text)
            if delete_habit(user_id, habit_id):
                bot.send_message(message.chat.id, f'Привычка с номером "{habit_id}" успешно удалена!')
            else:
                bot.send_message(message.chat.id, f'Привычка с номером "{habit_id}" не найдена.')
        except ValueError:
            bot.send_message(message.chat.id, 'Пожалуйста, введите корректный номер привычки.')

    @staticmethod
    def create_habit_name(message):
        """Обработчик ввода названия привычки."""
        habit_name = message.text
        bot.send_message(message.chat.id, 'Введите описание привычки:')
        bot.register_next_step_handler(message, Habit_bot.create_habit_description, habit_name=habit_name)

    @staticmethod
    def create_habit_description(message, habit_name: str):
        """Обработчик ввода описания привычки."""
        habit_description = message.text
        bot.send_message(message.chat.id, 'Введите единицу измерения привычки:')
        bot.register_next_step_handler(message, Habit_bot.create_habit_metric, habit_name=habit_name,
                                       habit_description=habit_description)


    @staticmethod
    def create_habit_metric(message, habit_name: str, habit_description: str):
        """Обработчик ввода единицы измерения привычки."""
        habit_metric = message.text
        bot.send_message(message.chat.id, 'Введите целевую дату привычки (в формате ДД.ММ.ГГГГ):')
        bot.register_next_step_handler(message, Habit_bot.create_habit_target_date, habit_name=habit_name,
                                       habit_description=habit_description, habit_metric=habit_metric)

    @staticmethod
    def create_habit_target_date(message, habit_name: str, habit_description: str, habit_metric: str):
        """Обработчик ввода целевой даты привычки."""
        user_id = message.from_user.id
        try:
            target_date = datetime.strptime(message.text, '%d.%m.%Y')
            habit = Habit(name=habit_name, description=habit_description, metric=habit_metric, target_date=target_date)
            add_habit(user_id, habit.name, habit.description, habit.metric, habit.target_date)
            bot.send_message(message.chat.id, f'Привычка "{habit.name}" успешно создана!')
        except ValueError:
            bot.send_message(message.chat.id, 'Пожалуйста, введите дату в формате ДД.ММ.ГГГГ.')
            bot.register_next_step_handler(message, Habit_bot.create_habit_target_date, habit_name=habit_name,
                                           habit_description=habit_description, habit_metric=habit_metric)

    @staticmethod
    def execute_habit_name(message):
        """Обработчик ввода ID привычки для выполнения."""
        user_id = message.from_user.id
        try:
            habit_id = int(message.text)
            habits = get_habits(user_id)
            habit = next((h for h in habits if h['id'] == habit_id), None)
            if habit:
                bot.send_message(message.chat.id, 'Введите прогресс выполнения привычки:')
                bot.register_next_step_handler(message, Habit_bot.execute_habit_progress, user_id=user_id,
                                               habit_id=habit_id)
            else:
                bot.send_message(message.chat.id, f'Привычка с номером "{habit_id}" не найдена.')
        except ValueError:
            bot.send_message(message.chat.id, 'Пожалуйста, введите корректный номер привычки.')

    @staticmethod
    def execute_habit_progress(message, user_id: int, habit_id: int):
        """Обработчик ввода прогресса выполнения привычки."""
        try:
            progress = message.text
            progress_date = datetime.now().strftime('%d.%m.%Y')
            add_habit_progress(habit_id, progress_date, progress)
            bot.send_message(message.chat.id, f'Выполнение привычки успешно зафиксировано!')
        except Exception as e:
            bot.send_message(message.chat.id, f'Произошла ошибка: {e}')

    @staticmethod
    def view_habit_progress_id(message):
        """Обработчик ввода ID привычки для просмотра прогресса."""
        try:
            habit_id = int(message.text)
            Habit_bot.view_habit_progress(message, habit_id=habit_id)
        except ValueError:
            bot.send_message(message.chat.id, 'Пожалуйста, введите корректный номер привычки.')

    @staticmethod
    def view_habit_progress(message, habit_id: int):
        """Обработчик ввода прогресса выполнения привычки."""
        habit_progress = get_habit_progress(habit_id=habit_id)
        if habit_progress:
            total_progress = 0
            today_progress = 0
            today_date = datetime.now().strftime('%d.%m.%Y')

            for habit in habit_progress:
                total_progress += int(habit["progress"])
                if habit["progress_date"] == today_date:
                    today_progress += int(habit["progress"])

            progress_str = '\n\n'.join(
                [f'Дата: {habit["progress_date"]}\nПрогресс: {habit["progress"]}' for habit in habit_progress])

            summary_str = (
                f'Ваш общий прогресс: {total_progress}\n'
                f'Прогресс за сегодня ({today_date}): {today_progress}\n\n'
                f'Детали прогресса:\n\n{progress_str}'
            )

            bot.send_message(message.chat.id, summary_str)
        else:
            bot.send_message(message.chat.id, 'У вас нулевой прогресс.')

# Запускаем бота
bot.polling(none_stop=True, interval=0)