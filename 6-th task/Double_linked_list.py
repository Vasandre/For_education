from typing import Optional


class DLNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev


# заполнение двусвязанного списка значениями из подаваемого списка
def create_doubly_linked_list(numbers: list) -> DLNode:
    head = None
    tail = None

    if numbers:
        current = DLNode(numbers[0])
        head = current
        current.prev = tail

        for item in numbers[1:]:
            current.next = DLNode(item)
            current.next.prev = current
            current = current.next

    return head


# вывод двусвязанного списка в виде обычного списка
def get_values_from_doubly_linked_list(head: Optional[DLNode]) -> list:
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


# вывод двусвязанного списка в виде обычного списка
def reverse_doubly_linked_list(tail: Optional[DLNode]) -> list:
    result = []

    while tail:
        result.append(tail.val)
        tail = tail.prev

    return result


# функция, удаляющая нод по порядковому номеру (возвращает нод)
def remove_node(head: DLNode, nodenum: int) -> DLNode:
    current = head

    count = 1
    while current:
        if (count == nodenum) and (current.prev is None):
            head = current.next

        elif (count == nodenum) and (current.next is None):
            current.prev.next = current.next
            current.prev = None

        elif count == nodenum:
            current.prev.next = current.next
            current.next.prev = current.prev

        current = current.next
        count += 1

    return head


# функция, добавляющая нод по порядковому номеру
def add_node(head: DLNode, nodenum: int) -> DLNode:
    current = head
    count = 1

    new_node = DLNode(nodenum)

    while current:

        if (count == nodenum) and (current.prev is None):
            next_node = head
            head = new_node
            new_node.prev = None
            new_node.next = next_node

        elif count == nodenum:

            next_node = current

            current.prev.next = new_node
            new_node.prev = current.prev

            new_node.next = next_node
            current.prev = new_node

        elif (nodenum > count) and (current.next is None):
            current.next = new_node
            new_node.next = None
            current.next.prev = current

        current = current.next
        count += 1

    return head


# функция разворачивающая список
def inverse_list(head: DLNode) -> DLNode:
    current = head
    next_node = None
    current_node = None


    while current:
        next_node = current.next
        current_node = current
        current.next = current.prev
        current.prev = current_node.prev

        current = next_node

    return current_node


node_head = create_doubly_linked_list([1, 3, 4, 5, 6])
