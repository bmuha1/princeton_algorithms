#!/usr/bin/python3
# Implement bottom-up merge sort
# O(nlog(n))


def merge(a, temp, low, mid, high):
    # Merge two sorted sublists
    i = k = low
    j = mid + 1
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
        k += 1
    while i < len(a) and i <= mid:
        temp[k] = a[i]
        i += 1
        k += 1
    for i in range(low, high + 1):
        a[i] = temp[i]
    print(a)


def bottom_up_merge(a):
    # Implement bottom-up merge sort
    low = 0
    high = len(a) - 1
    temp = a.copy()
    m = 1
    while m <= high - low:
        for i in range(low, high, m * 2):
            merge(a, temp, i, i + m - 1, min(i + m * 2 - 1, high))
        m *= 2


if __name__ == '__main__':
    a = [7, 10, 5, 3, 8, 4, 2, 9, 6, 1]
    print(a)
    bottom_up_merge(a)
