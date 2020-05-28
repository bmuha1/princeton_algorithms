#!/usr/bin/python3
# Implement selection sort
# O(n^2)


def selection_sort(a):
    # Implement selection sort
    length = len(a)
    for i in range(length):
        min = i
        for j in range(i + 1, length):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
        print(a)


if __name__ == '__main__':
    a = [7, 10, 5, 3, 8, 4, 2, 9, 6, 1]
    print(a)
    selection_sort(a)
