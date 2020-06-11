#!/usr/bin/python3
# Select the kth largest element in an array
# O(n) average
from random import randint


def select(a, k):
    # Select the kth largest element in an array
    shuffle(a)
    low, high = 0, len(a) - 1
    k_index = len(a) - k
    while low < high:
        j = partition(a, low, high)
        if j < k_index:
            low = j + 1
        elif j > k_index:
            high = j - 1
        else:
            return a[k_index]
    return a[k_index]


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
    return j


def shuffle(a):
    # Implement Knuth shuffle
    for i in range(len(a)):
        r = randint(0, i)
        a[i], a[r] = a[r], a[i]


if __name__ == '__main__':
    a = [7, 10, 5, 3, 8, 4, 2, 9, 6, 1]
    print(a)

    for k in range(1, 11):
        print('k:', k, 'kth highest:', select(a, k))
