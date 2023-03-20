"""
You're given the head of a Singly Linked List whose nodes are in sorted order with respect to their values.
Function has to return a modified version of the Linked List that doesn't contain any nodes with duplicate values.
The Linked List should be modified in place and the modified Linked List should still have its nodes sorted with
respect to their values.
Sample input:                                               |       Sample Output:
linked_list = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6     |     1 -> 3 -> 4 -> 5 -> 6  # the head node with value 1
"""


class Node:
    def __init__(self, val=0):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def remove_duplicates(self):
        current_el = self.head
        while current_el is not None:
            next_el = current_el.next
            while next_el is not None and current_el.value == next_el.value:
                next_el = next_el.next
            current_el.next = next_el
            current_el = next_el

    def append(self, element):
        current = self.head
        if current:
            while current.next is not None:
                current = current.next
            current.next = element
        else:
            self.head = element

    def __str__(self):
        s = ""
        current = self.head
        while current.next is not None:
            s += f"{current.value} -> "
            current = current.next
        s = s.rstrip("-> ")
        return s


e1 = Node(1)
tab = [Node(1), Node(3), Node(4), Node(4), Node(4), Node(5), Node(6), Node(6)]
L = LinkedList(e1)
for el in tab:
    L.append(el)
print(L)
L.remove_duplicates()
print(L)
