#!/usr/bin/python3
# Implement merge sort
# O(nlog(n))


def merge_sort(a):
    # Implement merge sort
    if len(a) < 2:
        return
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1
    print(a)


if __name__ == '__main__':
    a = [7, 10, 5, 3, 8, 4, 2, 9, 6, 1]
    print(a)
    merge_sort(a)
