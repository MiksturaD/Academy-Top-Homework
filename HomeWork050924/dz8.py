# Задание 1
# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск
# сотрудника по фамилии, вывод информации обо всех
# сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность
# сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из
# программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте
# программы происходит загрузка списка сотрудников из
# указанного пользователем файла.
# Python


# Определяем класс Employee для представления сотрудника
class Employee:
    # Конструктор класса, который инициализирует атрибуты сотрудника
    def __init__(self):
        with open('employees.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        self.id: int = len(lines) # Уникальный идентификатор сотрудника
        self.name = input('Введите имя нового сотрудника: ')
        self.surname = input('Введите фамилию нового сотрудника: ')
        self.age = input('Введите возраст нового сотрудника: ')


    def print_employee(self):
        print(f'ID сотрудника - {self.id}')
        print(f'Имя сотрудника - {self.name}')
        print(f'Фамилия сотрудника - {self.surname}')
        print(f'Возраст сотрудника - {self.age}')


    def save_employee(self):
        with open('employees.txt', 'a', encoding='utf-8') as f:
            f.write(f'{self.id},{self.name},{self.surname},{self.age}\n')
            self.id += 1


    def show_employee(self):
        with open('employees.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(lines)

    def delete_employee(self):
        delete_id: int = int(input('Введите ID сотрудника для удаления записи о нем: '))
        with open('employees.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        with open('employees.txt', 'w', encoding='utf-8') as f:
            for line in lines:
                employee_id = int(line.split(',')[0])
                if employee_id != delete_id:
                    f.write(line)

    def search_by_letter(self):
        search_letter: str = input('Введите первую буквы фамилии для поиска: ')
        with open('employees.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.split(',')
                if len(parts) > 1 and parts[2][0].strip() == search_letter:
                    print(line)


    def search_by_surname(self):
        search_family: str = input('Введите фамилию для поиска: ')
        with open('employees.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.split(',')
                if len(parts) > 1 and parts[2].strip() == search_family:
                    print(line)

    def search_by_age(self):
        search_age: str = input('Введите возраст для поиска: ')
        with open('employees.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.split(',')
                if len(parts) > 1 and parts[3].strip() == search_age:
                    print(line)


a = Employee()

a.print_employee()
a.save_employee()
a.show_employee()
a.delete_employee()
a.search_by_letter()
a.search_by_age()
a.search_by_surname()
