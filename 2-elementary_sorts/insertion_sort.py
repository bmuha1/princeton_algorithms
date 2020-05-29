#!/usr/bin/python3
# Implement insertion sort
# O(n^2)


def insertion_sort(a):
    # Implement insertion sort
    for i in range(len(a)):
        for j in range(i, 0, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
        print(a)


if __name__ == '__main__':
    a = [7, 10, 5, 3, 8, 4, 2, 9, 6, 1]
    print(a)
    insertion_sort(a)
