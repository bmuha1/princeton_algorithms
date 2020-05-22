#!/usr/bin/python3
# Implement deque using linked list


class Node:
    # Implement node
    def __init__(self, s, prev=None, next=None):
        # Initialize node
        self.item = s
        self.prev = prev
        self.next = next

    def __str__(self):
        # Print a node
        return str(self.item)


class Deque:
    # Implement deque using linked list
    def __init__(self):
        # Initialize deque
        self.head = None
        self.tail = None

    def is_empty(self):
        # Is the deque empty?
        return self.head is None

    def size(self):
        # Return the number of items on the deque
        size = 0
        temp = self.head
        while temp:
            size += 1
            temp = temp.next
        return size

    def add_first(self, item):
        # Add the item to the front
        if not item:
            raise TypeError('Illegal argument')
        new = Node(item, None, self.head)
        if self.head:
            self.head.prev = new
        self.head = new
        if not self.tail:
            self.tail = new

    def add_last(self, item):
        # Add the item to the back
        if not item:
            raise TypeError('Illegal argument')
        new = Node(item, self.tail, None)
        if self.tail:
            self.tail.next = new
        self.tail = new
        if not self.head:
            self.head = new

    def remove_first(self):
        # Remove and return the item from the front
        if self.is_empty():
            raise IndexError('No such element')
        first = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return first.item

    def remove_last(self):
        # Remove and return the item from the back
        if self.is_empty():
            raise IndexError('No such element')
        last = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        return last.item

    def __str__(self):
        # Print all the items in the deque
        if self.is_empty():
            return 'Deque is empty'
        temp = self.head
        s = str(temp)
        while temp.next:
            temp = temp.next
            s += ', ' + str(temp)
        return s


if __name__ == '__main__':
    l = Deque()
    print(l, l.size(), l.is_empty())
    l.add_last('bat')
    print(l, l.size(), l.is_empty())
    l.add_first('cat')
    print(l, l.size(), l.is_empty())
    l.add_first('ape')
    print(l, l.size(), l.is_empty())
    print(l.remove_last())
    print(l, l.size(), l.is_empty())
    print(l.remove_first())
    print(l, l.size(), l.is_empty())
    print(l.remove_first())
    print(l, l.size(), l.is_empty())
