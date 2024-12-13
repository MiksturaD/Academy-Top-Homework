import threading
from datetime import datetime
import telebot
from telebot import types
from list import token
import schedule
import time
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
    markup = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text="Создание привычки", callback_data='create_habit')
    button_2 = types.InlineKeyboardButton(text="Список привычек", callback_data='view_habits')
    button_3 = types.InlineKeyboardButton(text="Удаление привычки", callback_data='delete_habit')
    button_4 = types.InlineKeyboardButton(text="Выполнение привычки", callback_data='execute_habit')
    button_5 = types.InlineKeyboardButton(text="Показать текущий прогресс выполнения привычки", callback_data='view_progress')
    button_6 = types.InlineKeyboardButton(text="Написать автору", callback_data='feedback')

    markup.add(button_1, button_2, button_3, button_4, button_5, button_6)

    bot.send_message(m.chat.id, 'Нажми:'
                                '\nСоздание привычки - для создания новой привычки'
                                '\nСписок привычек - для просмотра существующих привычек'
                                '\nУдаление привычки - для удаления ненужной привычки'
                                '\nВыполнение привычки - для фиксации действий по твоей привычке'
                                '\nПоказать текущий прогресс выполнения привычки - для просмотра прогресса выполнения привычки',
                     reply_markup=markup)

# Обработчик callback_query
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'create_habit':
        bot.send_message(call.message.chat.id, 'Напиши название привычки:')
        bot.register_next_step_handler(call.message, Habit_bot.create_habit_name)
    elif call.data == 'view_habits':
        Habit_bot.view_habits(call.message)
    elif call.data == 'delete_habit':
        bot.send_message(call.message.chat.id, 'Введи ID привычки для удаления:')
        bot.register_next_step_handler(call.message, Habit_bot.delete_habit_name)
    elif call.data == 'execute_habit':
        bot.send_message(call.message.chat.id, 'Введи ID привычки, которую хочешь выполнить:')
        bot.register_next_step_handler(call.message, Habit_bot.execute_habit_name)
    elif call.data == 'view_progress':
        bot.send_message(call.message.chat.id, 'Введи ID привычки, которую хочешь посмотреть:')
        bot.register_next_step_handler(call.message, Habit_bot.view_habit_progress_id)
    elif call.data == 'feedback':
        bot.send_message(call.message.chat.id, 'Напиши, что ты хочешь сказать автору бота')
        bot.register_next_step_handler(call.message, Habit_bot.feedback)

class Habit_bot:

    def __init__(self, name: str, description: str = None, metric: str = None, target_date: str = None) -> None:
        self.name = name
        self.description = description
        self.metric = metric
        self.target_date = target_date

    def __repr__(self) -> str:
        return (f'Название: {self.name}\nОписание: {self.description}\nЕдиница измерения: {self.metric}\n'
                f'Дата до которой ты хочешь выполнять привычку: {self.target_date}')

    @staticmethod
    def feedback(message):
        author_user_id = "332286763"
        user_message = message.text
        bot.send_message(author_user_id, f'Вам написал фанат вашего бота - {message.from_user.id} '
                                         f'И вот что он пишет: {user_message}')
        bot.send_message(message.chat.id, 'Сообщение отправлено автору бота')

    @staticmethod
    def view_habits(message):
        """Отображение списка привычек."""
        user_id = message.from_user.id
        habits = get_habits(user_id)
        if habits:
            habits_str = '\n\n'.join(
                [f'ID: {habit["id"]}\nНазвание: {habit["name"]}\nОписание: {habit["description"]}\n'
                 f'Единица измерения: {habit["metric"]}\nДата до которой ты хочешь выполнять привычку:'
                 f' {habit["target_date"]}' for habit in habits])
            bot.send_message(message.chat.id, f'Твои привычки:\n\n{habits_str}')
        else:
            bot.send_message(message.chat.id, 'У тебя нет ни одной привычки (А надо бы, чтобы были!).')


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
            bot.send_message(message.chat.id, 'Напиши корректный номер привычки.')

    @staticmethod
    def create_habit_name(message):
        """Обработчик ввода названия привычки."""
        habit_name = message.text
        bot.send_message(message.chat.id, 'Придумай и напиши о чем твоя привычка:')
        bot.register_next_step_handler(message, Habit_bot.create_habit_description, habit_name=habit_name)

    @staticmethod
    def create_habit_description(message, habit_name: str):
        """Обработчик ввода описания привычки."""
        habit_description = message.text
        bot.send_message(message.chat.id, 'В чем будут измеряться действия по привычке: '
                                          '(например для привычки "пить воду" - мл или стаканы)')
        bot.register_next_step_handler(message, Habit_bot.create_habit_metric, habit_name=habit_name,
                                       habit_description=habit_description)

    @staticmethod
    def create_habit_metric(message, habit_name: str, habit_description: str):
        """Обработчик ввода единицы измерения привычки."""
        habit_metric = message.text
        bot.send_message(message.chat.id, 'Напиши дату до которой ты хочешь эту привычку фиксировать'
                                          ' (в формате ДД.ММ.ГГГГ):')
        bot.register_next_step_handler(message, Habit_bot.create_habit_target_date, habit_name=habit_name,
                                       habit_description=habit_description, habit_metric=habit_metric)

    @staticmethod
    def create_habit_target_date(message, habit_name: str, habit_description: str, habit_metric: str):
        """Обработчик ввода целевой даты привычки."""
        user_id = message.from_user.id
        try:
            target_date = datetime.strptime(message.text, '%d.%m.%Y')
            now = datetime.now()
            delta = target_date - now
            if delta.total_seconds() <= 0:
                bot.send_message(message.chat.id, 'Этот день уже прожит тобой, попробуй еще раз.')
                bot.register_next_step_handler(message, Habit_bot.create_habit_target_date, habit_name=habit_name,
                                          habit_description=habit_description, habit_metric=habit_metric)
            else:
                habit = Habit(name=habit_name, description=habit_description, metric=habit_metric,
                              target_date=target_date)
                add_habit(user_id, habit.name, habit.description, habit.metric, habit.target_date)
                bot.send_message(message.chat.id, 'Хочешь установить ежедневное напоминание о том, что надо '
                                                  'выполнять привычку?(ответ да или нет)')
                bot.register_next_step_handler(message, Habit_bot.ask_for_reminder, habit=habit)
        except ValueError:
            bot.send_message(message.chat.id, 'Нет, так не пойдет, напиши дату в формате ДД.ММ.ГГГГ.')
            bot.register_next_step_handler(message, Habit_bot.create_habit_target_date, habit_name=habit_name,
                                           habit_description=habit_description, habit_metric=habit_metric)

    @staticmethod
    def ask_for_reminder(message, habit):
        """Обработчик ответа на вопрос о создании напоминания."""
        if message.text.upper() == 'ДА':
            bot.send_message(message.chat.id, 'Придумай название напоминания:')
            bot.register_next_step_handler(message, Habit_bot.set_reminder_name, habit=habit)
        else:
            bot.send_message(message.chat.id, f'Привычка "{habit.name}" успешно создана!')

    @staticmethod
    def set_reminder_name(message, habit):
        """ Функция, которую вызывает обработчик команды /reminder для установки названия напоминания"""
        reminder_name = message.text
        bot.send_message(message.chat.id, 'В какую дату и время начнем слать тебе напоминания о привычке? '
                                          'в формате ДД.ММ.ГГГГ чч:мм:сс.')
        bot.register_next_step_handler(message, Habit_bot.reminder_set, reminder_name=reminder_name, habit=habit)

    @staticmethod
    def reminder_set(message, reminder_name: str, habit):
        """ Функция для установки напоминания"""
        try:
            # Преобразуем введенную пользователем дату и время в формат datetime
            reminder_time = datetime.strptime(message.text, '%d.%m.%Y %H:%M:%S')
            now = datetime.now()
            delta = reminder_time - now
            # Если введенная пользователем дата и время уже прошли, выводим сообщение об ошибке
            if delta.total_seconds() <= 0:
                bot.send_message(message.chat.id, 'Не не не, эта дата уже в прошлом! Попробуй еще раз.')
                # Если пользователь ввел корректную дату и время, устанавливаем напоминание и запускаем таймер
            else:
                bot.send_message(message.chat.id, f'Напоминание {reminder_name} установлено на - {reminder_time}')
                # Планируем напоминание
                chat_id = message.chat.id
                Habit_bot.schedule_reminder(chat_id, reminder_name, reminder_time)
            # Если пользователь ввел некорректную дату и время, выводим сообщение об ошибке
        except ValueError:
            bot.send_message(message.chat.id, 'Не правильный ввод даты, давай ка еще раз в '
                                              'формате ДД.ММ.ГГГГ чч:мм:сс')

    @staticmethod
    def send_reminder(chat_id, reminder_name):
        """Функция, которая отправляет напоминание пользователю"""
        bot.send_message(chat_id, f'Время для - {reminder_name}, не забудь зафиксировать результат!')

    @staticmethod
    def schedule_reminder(chat_id, reminder_name, reminder_time):
        """Функция для планирования напоминания в определенное время"""

        def job():
            Habit_bot.send_reminder(chat_id, reminder_name)

        # Преобразуем время в формат, понятный schedule
        schedule_time = reminder_time.strftime('%H:%M')
        schedule.every().day.at(schedule_time).do(job)

    @staticmethod
    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)

    # Запуск планировщика в отдельном потоке
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()

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
            bot.send_message(message.chat.id, 'Неа, введи корректный номер привычки.')

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
            bot.send_message(message.chat.id, 'Неа, введи корректный номер привычки.')

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
                f'Общий прогресс по привычке: {total_progress}\n'
                f'Прогресс за сегодня ({today_date}): {today_progress}\n\n'
                f'Детали прогресса:\n\n{progress_str}'
            )

            bot.send_message(message.chat.id, summary_str)
        else:
            bot.send_message(message.chat.id, 'У тебя нулевой прогресс.')

# Запускаем бота
bot.polling(none_stop=True, interval=0)
