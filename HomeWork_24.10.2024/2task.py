from __future__ import annotations
from abc import ABC, abstractmethod

# Абстрактный класс Продукта
class Product(ABC):
    """
    Интерфейс Продукта объявляет операции, которые должны выполнять все конкретные продукты.
    """

    @abstractmethod
    def get_type(self) -> str:
        pass
    @abstractmethod
    def get_sauce(self) -> str:
        pass

    @abstractmethod
    def get_filling(self) -> str:
        pass

    @abstractmethod
    def get_additives(self) -> list:
        pass

# Конкретный Продукт 1
class ConcreteProduct1(Product):
    def get_type(self) -> str:
        return "Spaghetti"

    def get_sauce(self) -> str:
        return "Tomato"

    def get_filling(self) -> str:
        return "Meatballs"

    def get_additives(self) -> list:
        return ["Basil", "Parmesan"]

# Конкретный Продукт 2
class ConcreteProduct2(Product):
    def get_type(self) -> str:
        return "Penne"

    def get_sauce(self) -> str:
        return "Alfredo"

    def get_filling(self) -> str:
        return "Chicken"

    def get_additives(self) -> list:
        return ["Chives", "Cheddar"]

# Конкретный Продукт 3
class ConcreteProduct3(Product):
    def get_type(self) -> str:
        return "Fettuccine"

    def get_sauce(self) -> str:
        return "Shrimp"

    def get_additives(self) -> list:
        return ["Parsley", "Lemon"]
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def prepare_pasta(self) -> str:
        product = self.factory_method()
        result = (f"Preparing {product.get_type()} pasta with {product.get_sauce()} sauce, "
                  f"{product.get_filling()} filling, and {', '.join(product.get_additives())} additives.")
        return result

# Конкретный Создатель 1
class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()

# Конкретный Создатель 2
class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()

# Конкретный Создатель 3
class ConcreteCreator3(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct3()

# Клиентский код
def client_code(creator: Creator) -> None:
    print(creator.prepare_pasta())

# Запуск приложения
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
    print("\n")

    print("App: Launched with the ConcreteCreator3.")
    client_code(ConcreteCreator3())