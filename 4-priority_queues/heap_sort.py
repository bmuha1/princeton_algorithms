#!/usr/bin/python3
# Implement heap sort
# O(nlog(n))


class MaxHeap:
    # Implement max heap
    def __init__(self):
        # Initialize max heap
        self.heap = [0, 'S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
        self.n = 11

    def build(self):
        # Build heap using bottom-up method
        k = self.n // 2
        while k >= 1:
            self.sink(k)
            k -= 1

    def sort(self):
        # Remove max, one at a time
        while self.n > 1:
            self.heap[1], self.heap[self.n] = self.heap[self.n], self.heap[1]
            self.n -= 1
            self.sink(1)

    def swim(self, k):
        # Move node up to maintain binary heap property
        while k > 1 and self.heap[k // 2] < self.heap[k]:
            self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
            k //= 2

    def sink(self, k):
        # Move node down to maintain binary heap property
        while k * 2 <= self.n:
            j = 2 * k
            if j < self.n and self.heap[j] < self.heap[j + 1]:
                j += 1
            if self.heap[k] >= self.heap[j]:
                break
            self.heap[k], self.heap[j] = self.heap[j], self.heap[k]
            k = j

    def insert(self, x):
        # Insert node
        self.heap.append(x)
        self.n += 1
        self.swim(self.n)

    def delete_max(self):
        # Delete maximum node
        if self.n < 1:
            print('Heap is empty')
        else:
            max = self.heap[1]
            self.heap[1] = self.heap[self.n]
            self.n -= 1
            self.heap.pop()
            self.sink(1)
            return max

    def __str__(self):
        # Print max heap
        return str(self.heap[1:])


if __name__ == '__main__':
    pq = MaxHeap()
    print(pq)
    pq.build()
    print(pq)
    pq.sort()
    print(pq)
