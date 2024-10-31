import copy  # Импортируем модуль для глубокого копирования объектов
class Prototype:
    """
    Класс Prototype предоставляет шаблон для создания объектов через их клонирование.
    """
    def __init__(self):
        """
        Инициализатор класса Prototype.
        Создается словарь _objects для хранения именованных объектов.
        """
        self._objects = {}

    def register_object(self, name, obj):
        """
        Метод для регистрации объекта с именем.
        :param name: Имя объекта
        :param obj: Объект для регистрации
        """
        self._objects[name] = obj

    def unregister_object(self, name):
        """
        Метод для удаления зарегистрированного объекта по имени.
        :param name: Имя объекта для удаления
        """
        del self._objects[name]

    def clone(self, name, **kwargs):
        """
        Метод для клонирования объекта по имени с возможностью передачи дополнительных аргументов.
        :param name: Имя объекта для клонирования
        :param kwargs: Дополнительные аргументы для клонированного объекта
        :return: Клонированный объект
        """
        cloned_obj = copy.deepcopy(self._objects.get(name))
        cloned_obj.__dict__.update(kwargs)
        return cloned_obj


class Car:
    """
    Класс Car представляет собой автомобиль с моделью и цветом.
    """
    def __init__(self, model, color):
        """
        Инициализатор класса Car.
        :param model: Модель автомобиля
        :param color: Цвет автомобиля
        """
        self.model = model
        self.color = color

    def __str__(self):
        """
        Метод для представления объекта в виде строки.
        :return: Строковое представление автомобиля
        """
        return f"{self.color} {self.model}"


# Тестирование
prototype = Prototype()
prototype.register_object('car1', Car('Toyota', 'Red'))

car_clone = prototype.clone('car1', color='Blue')
print(car_clone)  # Вывод: Blue Toyota
