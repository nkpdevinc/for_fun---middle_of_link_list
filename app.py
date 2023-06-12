'''
For fun, https://leetcode.com/
876. Middle of the Linked List
'''

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    # Сначала создаем методы для работы ВНУТРИ Объекта связанного списка, извне их смысла применять нет, они для работы с cur_node=self.head
    # --- то есть для работы с ТЕКУЩЕЙ node вызванной в LinkedList      
    # Get метод для возврата данных текущего нода
    def get_data(self):
        return self.data
    
    # Get метод для возврата ссылки текущего Node на следующий элемент
    def get_next(self):
        return self.next

    # Set метод замены задающий новые данные для текущего node
    def set_data(self, data):
        self.data = data
    
    # Set метод замены задающий новую ссылку для текущего node
    def set_next(self, next):
        self.next = next

# Формируем сам список        
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    # Создаем методы для обращения извне
    # Метод добавления в список данных. Если головного элемента не существует то мы создаем его из передаваемых данных, иначе переходим в начало
    # списка и запускаем цикл, который идет пока ссылка на следующий node не будет None(то есть дойдем до конца списка), и вместо этого пустого
    # последнего элемента(None) мы записываем переданные в список извне данные  
    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.length += 1
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            self.length += 1
    

    # Return the middle node of the linked list. If there are two middle nodes, return the second middle node.
    def middle_node(self):
        slow_ptr = self.head
        fast_ptr = self.head
        if self.head is not None:
            while (fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            if self.length % 2 == 0:
                slow_ptr = slow_ptr.next
            print("The middle element is: ", slow_ptr.data)


llist = LinkedList()
llist.add_node(6)
llist.add_node(5)
llist.add_node(4)
llist.add_node(3)
llist.add_node(2)
llist.add_node(1)
llist.middle_node()