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
        self.employees = []
        self.file_name = 'employees.txt'
        self.load_employees()

    def load_employees(self):
        try:
            with open('employees.txt', 'r', encoding='utf-8') as f:
                data = f.readlines()
                for item in data:
                    emp = Employee(item[id], item['name'], item['surname'], item['age'])
                    self.employees.append(emp)
        except FileNotFoundError:
            pass

    # def input_employee(self):
    #     self.name = input('Введите имя нового сотрудника: ')
    #     self.surname = input('Введите фамилию нового сотрудника: ')
    #     self.age = input('Введите возраст нового сотрудника: ')


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

    def search_by_surname(self):
        search_family: str = input('Введите фамилию для поиска: ')
        with open('employees.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.split(',')
                if len(parts) > 1 and parts[1].strip() == search_family:
                    print(line)

    def find_employee_by_surname(self):
        # Ищем сотрудника по фамилии
        surname = input("Введите фамилию сотрудника для поиска: ")
        # Ищем в цикле по списку сотрудников
        found = [emp for emp in self.employees if emp.surname.lower() == surname.lower()]
        # Находим сотрудника и выводим инфу о нем
        if found:
            for emp in found:
                print(f"{emp.id}. {emp.name} {emp.surname} ({emp.age} лет)")
        else:
            # Если не находим сотрудника - выводим сообщение
            print("Сотрудник не найден")

a = Employee()
# a.input_employee()
a.print_employee()
a.save_employee()
a.show_employee()
# a.delete_employee()
a.find_employee_by_surname()
