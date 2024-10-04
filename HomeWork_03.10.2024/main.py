from DualLinkedList import DualLinkedList
from LinkedList import LinkedList
from Menu import Menu

ll = LinkedList()

menu = Menu()
menu.add_item('Добавить элемент в список.', ll.add, value=None)
menu.add_item('Удалить элемент из списка.', ll.remove)
menu.add_item('Показать содержимое списка.', ll.show)
# menu.add_item('Проверить есть ли значение в списке.')
menu.add_item('Заменить значение в списке.', ll.update, value=None)

while True:
	menu.print()
	menu.choose()

