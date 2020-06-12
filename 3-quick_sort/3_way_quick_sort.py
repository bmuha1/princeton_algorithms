#!/usr/bin/python3
# Implement 3-way quick sort with shuffle
# O(nlog(n))
from random import randint


def quick_sort_3_way(a):
    # Implement 3-way quick sort with shuffle
    shuffle(a)
    print(a)
    sort(a, 0, len(a) - 1)
    print(a)


def sort(a, low, high):
    # Quick sort helper method
    if high <= low:
        return
    i, lt, gt = low, low, high
    v = a[low]
    while i <= gt:
        if a[i] < v:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif a[i] > v:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1
    sort(a, low, lt - 1)
    sort(a, gt + 1, high)


def shuffle(a):
    # Implement Knuth shuffle
    for i in range(len(a)):
        r = randint(0, i)
        a[i], a[r] = a[r], a[i]


if __name__ == '__main__':
    a = [2, 1, 3, 3, 1, 2, 1, 2, 3, 3, 1, 2, 1, 3, 1, 2, 3, 2, 2, 1, 1, 3, 3]
    print(a)
    quick_sort_3_way(a)
