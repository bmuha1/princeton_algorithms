#!/usr/bin/python3
# Implement randomized queue using linked list
from random import randint


class Node:
    # Implement node
    def __init__(self, s, next=None):
        # Initialize node
        self.item = s
        self.next = next


class RandomizedQueue:
    # Implement randomized queue using linked list
    def __init__(self):
        # Initialize linked list
        self.first = None
        self.last = None

    def __str__(self):
        # Print queue
        if self.first is None:
            return 'Empty list'
        current = self.first
        string = str(current.item)
        while current.next is not None:
            current = current.next
            string += ' ' + str(current.item)
        return string

    def is_empty(self):
        # Check if queue is empty
        return self.first is None

    def size(self):
        # Return the number of items
        size, temp = 0, self.first
        while temp:
            size += 1
            temp = temp.next
        return size

    def enqueue(self, s):
        # Add an item to the end of the queue
        old_last = self.last
        self.last = Node(s)
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last

    def dequeue(self):
        # Remove and return a random item
        if self.is_empty():
            return('No item to remove')
        index = randint(0, self.size() - 1)
        temp, prev = self.first, None
        while index:
            index -= 1
            prev = temp
            temp = temp.next
        if prev:
            prev.next = temp.next
        else:
            self.first = temp.next
        return temp.item

    def sample(self):
        # Return a random item
        if self.is_empty():
            return('No item to sample')
        index = randint(0, self.size() - 1)
        temp = self.first
        while index:
            index -= 1
            temp = temp.next
        return temp.item


if __name__ == '__main__':
    l = RandomizedQueue()
    for i in range(ord('A'), ord('I') + 1):
        l.enqueue(chr(i))
    print(l)

    sample = set()
    while len(sample) < 5:
        s = l.sample()
        if s not in sample:
            print('sample:', s)
        sample.add(s)

    while not l.is_empty():
        print(l)
        print('size:', l.size())
        print('remove:', l.dequeue())
    print(l)
