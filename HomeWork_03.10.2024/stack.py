# Задание 2
# Реализуйте класс стека для работы со строками (стек
# строк).
# Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки
# из стека.

class StringStack:
    def __init__(self, size):
        self.size = size
        self.items = []

    def push(self, item):
        if len(self.items) < self.size:
            self.items.append(item)
        else:
            raise IndexError("Стек переполнен")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")

    def count(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.size

    def clear(self):
        self.items = []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пуст")

# Пример использования:
stack = StringStack(3)
stack.push("Hello")
stack.push("World")
print(stack.count())
print(stack.peek())
print(stack.pop())
print(stack.is_empty())
stack.push("Python")
stack.push("Java")


# Задание 3
# Измените стек из второго задания, таким образом,
# чтобы его размер был нефиксированным.


class StringStack_inf_size:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)


    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")

    def count(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пуст")

# Пример использования:
stack = StringStack_inf_size()
stack.push("Hello")
stack.push("World")
stack.push("World1")
stack.push("World2")
stack.push("World4")
print(stack.count())
print(stack.peek())
print(stack.is_empty())  # Вывод: False
stack.push("Python")
print(stack.peek())