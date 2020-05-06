#!/usr/bin/python3
# Compare efficiency of different methods for solving the "three sum" problem


def three(arr):
    # Given n distinct integers, how many triples sum to zero?
    # O(n^3)
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == 0:
                    count += 1
    return count


def three_deluxe(arr):
    # Given n distinct integers, how many triples sum to zero?
    # O(n^2 log(n))
    sorted = arr.copy()
    sorted.sort()
    count = 0
    for i in range(len(sorted)):
        for j in range(i + 1, len(sorted)):
            left, right = 0, len(sorted) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if sorted[i] + sorted[j] + sorted[mid] > 0:
                    right = mid - 1
                elif sorted[i] + sorted[j] + sorted[mid] < 0:
                    left = mid + 1
                else:
                    if sorted[i] < sorted[j] < sorted[mid]:
                        count += 1
                    break
    return count

if __name__ == '__main__':
    arr = [30, -40, -20, -10, 40, 0, 10, 5]
    print(three(arr))
    print(three_deluxe(arr))
