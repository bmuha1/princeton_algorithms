#!/usr/bin/python3
# Implement linked stack of strings


class Node:
    # Implement node containing string
    def __init__(self, s, next=None):
        # Initialize node
        self.item = s
        self.next = next


class LinkedStackOfStrings:
    # Implement linked stack of strings
    def __init__(self):
        # Initialize linked list
        self.head = None

    def __str__(self):
        # Print linked stack of strings
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
        # Push a string onto the stack
        first = Node(s, self.head)
        self.head = first

    def is_empty(self):
        # Check if linked stack is empty
        return self.head is None


if __name__ == '__main__':
    l = LinkedStackOfStrings()
    l.push('to')
    l.push('be')
    l.push('or')
    l.push('not')
    l.push('to')
    print(l.pop())
    l.push('be')
    print(l.pop())
    print(l.pop())
    l.push('that')
    print(l.pop())
    print(l.pop())
    print(l.pop())
    l.push('is')
