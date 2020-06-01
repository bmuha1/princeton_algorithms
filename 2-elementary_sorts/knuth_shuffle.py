#!/usr/bin/python3
# Implement Knuth shuffle
# O(n)
from random import randint


def shuffle(a):
    # Implement Knuth shuffle
    for i in range(len(a)):
        r = randint(0, i)
        a[i], a[r] = a[r], a[i]
        print(a)


if __name__ == '__main__':
    a = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    shuffle(a)
