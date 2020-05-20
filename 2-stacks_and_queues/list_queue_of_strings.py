#!/usr/bin/python3
# Implement list queue of strings


class ListQueueOfStrings:
    # Implement list queue of strings
    def __init__(self):
        # Initialize list
        self.list = []

    def __str__(self):
        # Print linked queue of strings
        if not self.list:
            return 'Empty list'
        string = ''
        for i in range(len(self.list) - 1, -1, -1):
            string += self.list[i]
            if i != 0:
                string += ' '
        return string

    def dequeue(self):
        # Remove the item at the front of the queue
        return self.list.pop(0)

    def enqueue(self, s):
        # Add a string to the end of the queue
        self.list.append(s)

    def is_empty(self):
        # Check if linked queue is empty
        return len(self.list) == 0


if __name__ == '__main__':
    l = ListQueueOfStrings()
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
