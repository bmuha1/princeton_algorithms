#!/usr/bin/python3
# Implement linked queue of strings


class Node:
    # Implement node containing string
    def __init__(self, s, next=None):
        # Initialize node
        self.item = s
        self.next = next


class LinkedQueueOfStrings:
    # Implement linked queue of strings
    def __init__(self):
        # Initialize linked list
        self.first = None
        self.last = None

    def __str__(self):
        # Print linked queue of strings
        if self.first is None:
            return 'Empty list'
        current = self.first
        string = str(current.item)
        while current.next is not None:
            current = current.next
            string += ' ' + str(current.item)
        return string

    def dequeue(self):
        # Remove the item at the front of the queue
        item = self.first.item
        self.first = self.first.next
        if self.is_empty():
            self.last = None
        return item

    def enqueue(self, s):
        # Add a string to the end of the queue
        old_last = self.last
        self.last = Node(s)
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last

    def is_empty(self):
        # Check if linked queue is empty
        return self.first is None


if __name__ == '__main__':
    l = LinkedQueueOfStrings()
    l.enqueue('to')
    l.enqueue('be')
    l.enqueue('or')
    l.enqueue('not')
    l.enqueue('to')
    print(l.dequeue())
    l.enqueue('be')
    print(l.dequeue())
    print(l.dequeue())
    l.enqueue('that')
    print(l.dequeue())
    print(l.dequeue())
    print(l.dequeue())
    l.enqueue('is')
