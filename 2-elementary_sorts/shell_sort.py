#!/usr/bin/python3
# Implement shell sort
# O(n^(3/2)) worst case


def shell_sort(a):
    # Implement shell sort
    length, h = len(a), 1

    # 3x + 1 increment (1, 4, 13, 40, 121, 364, ...)
    while h < length / 3:
        h *= 3 + 1

    while h >= 1:
        # Insertion sort
        for i in range(h, length):
            for j in range(i, h - 1, -h):
                if a[j] < a[j - h]:
                    a[j], a[j - h] = a[j - h], a[j]
        print(a)
        h //= 3


if __name__ == '__main__':
    a = [7, 10, 5, 3, 8, 4, 2, 9, 6, 1]
    print(a)
    shell_sort(a)
    b = ['S', 'H', 'E', 'L', 'L', 'S', 'O', 'R',
         'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    print(b)
    shell_sort(b)
