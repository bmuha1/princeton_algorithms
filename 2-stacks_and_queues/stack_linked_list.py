#!/usr/bin/python3
# Implement stack using linked list


class Node:
    # Implement node
    def __init__(self, s, next=None):
        # Initialize node
        self.item = s
        self.next = next


class Stack:
    # Implement stack using linked list
    def __init__(self):
        # Initialize linked list
        self.head = None

    def __str__(self):
        # Print stack
        if self.head is None:
            return 'Empty list'
        current = self.head
        string = str(current.item)
        while current.next is not None:
            current = current.next
            string += ' ' + str(current.item)
        return string

    def pop(self):
        # Pop the first item
        item = self.head.item
        self.head = self.head.next
        return item

    def push(self, s):
        # Push an item onto the stack
        first = Node(s, self.head)
        self.head = first

    def is_empty(self):
        # Check if stack is empty
        return self.head is None


if __name__ == '__main__':
    l = Stack()
    l.push('to')
    l.push(2)
    l.push('or')
    l.push(3.5)
    l.push('to')
    print(l.pop())
    l.push(False)
    print(l.pop())
    print(l.pop())
    l.push('that')
    print(l.pop())
    print(l.pop())
    print(l.pop())
    l.push('is')
