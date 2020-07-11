#!/usr/bin/python3
# Implement binary heap
# O(log(n)) insert and delete


class MinHeap:
    # Implement max heap
    def __init__(self):
        # Initialize min heap
        self.heap = [0]
        self.n = 0

    def swim(self, k):
        # Move node up to maintain binary heap property
        while k > 1 and self.heap[k // 2] > self.heap[k]:
            self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
            k //= 2

    def sink(self, k):
        # Move node down to maintain binary heap property
        while k * 2 <= self.n:
            j = 2 * k
            if j < self.n and self.heap[j] > self.heap[j + 1]:
                j += 1
            if self.heap[k] <= self.heap[j]:
                break
            self.heap[k], self.heap[j] = self.heap[j], self.heap[k]
            k = j

    def insert(self, x):
        # Insert node
        self.heap.append(x)
        self.n += 1
        self.swim(self.n)

    def delete_min(self):
        # Delete minimum node
        if self.n < 1:
            print('Heap is empty')
        else:
            min = self.heap[1]
            self.heap[1] = self.heap[self.n]
            self.n -= 1
            self.heap.pop()
            self.sink(1)
            return min

    def __str__(self):
        # Print min heap
        return str(self.heap[1:])


if __name__ == '__main__':
    pq = MinHeap()
    pq.insert(3)
    pq.insert(8)
    pq.insert(1)
    pq.insert(10)
    pq.insert(6)
    pq.insert(7)
    pq.insert(5)
    pq.insert(2)
    pq.insert(9)
    pq.insert(4)
    print(pq)

    while pq.n > 1:
        pq.delete_min()
        print(pq)
