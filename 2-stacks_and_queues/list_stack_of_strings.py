#!/usr/bin/python3
# Implement list stack of strings


class ListStackOfStrings:
    # Implement list stack of strings
    def __init__(self):
        # Initialize linked list
        self.list = []

    def __str__(self):
        # Print linked stack of strings
        if not self.list:
            return 'Empty list'
        string = ''
        for i in range(len(self.list) - 1, -1, -1):
            string += self.list[i]
            if i != 0:
                string += ' '
        return string

    def pop(self):
        # Pop the first item
        return self.list.pop()

    def push(self, s):
        # Push a string onto the stack
        self.list.append(s)

    def is_empty(self):
        # Check if linked stack is empty
        return len(self.list) == 0

if __name__ == '__main__':
    l = ListStackOfStrings()
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