#!/usr/bin/python3
# Implement quick sort with shuffle
# O(nlog(n))
from random import randint


def quick_sort(a):
    # Implement quick sort with shuffle
    shuffle(a)
    print(a)
    sort(a, 0, len(a) - 1)


def sort(a, low, high):
    # Quick sort helper method
    if high <= low:
        return
    j = partition(a, low, high)
    sort(a, low, j - 1)
    sort(a, j + 1, high)


def partition(a, low, high):
    # Partition around a pivot
    i, j = low, high + 1
    while True:
        i += 1
        while a[i] < a[low]:
            if i == high:
                break
            i += 1
        j -= 1
        while a[low] < a[j]:
            if j == low:
                break
            j -= 1
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
    a[low], a[j] = a[j], a[low]
    print(a)
    return j


def shuffle(a):
    # Implement Knuth shuffle
    for i in range(len(a)):
        r = randint(0, i)
        a[i], a[r] = a[r], a[i]


if __name__ == '__main__':
    a = [7, 10, 5, 3, 8, 4, 2, 9, 6, 1]
    print(a)
    quick_sort(a)

    b = ['Q', 'U', 'I', 'C', 'K', 'S', 'O', 'R',
         'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    print(b)
    quick_sort(b)
