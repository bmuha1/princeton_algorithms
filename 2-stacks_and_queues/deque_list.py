#!/usr/bin/python3
# Implement deque using list


class Deque:
    # Implement deque using list
    def __init__(self):
        # Initialize deque
        self.list = []

    def is_empty(self):
        # Is the deque empty?
        return len(self.list) == 0

    def size(self):
        # Return the number of items on the deque
        return len(self.list)

    def add_first(self, item):
        # Add the item to the front
        if not item:
            raise TypeError('Illegal argument')
        self.list.insert(0, item)

    def add_last(self, item):
        # Add the item to the back
        if not item:
            raise TypeError('Illegal argument')
        self.list.append(item)

    def remove_first(self):
        # Remove and return the item from the front
        if self.is_empty():
            raise IndexError('No such element')
        return self.list.pop(0)

    def remove_last(self):
        # Remove and return the item from the back
        if self.is_empty():
            raise IndexError('No such element')
        return self.list.pop()

    def __str__(self):
        # Print all the items in the deque
        if self.is_empty():
            return 'Deque is empty'
        s = self.list[0]
        for i in range(1, self.size()):
            s += ', ' + self.list[i]
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
