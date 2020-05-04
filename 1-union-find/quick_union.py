#!/usr/bin/python3
# Implement quick union


class QuickUnion():
    def __init__(self, size):
        # Initialize list
        # O(n)
        self.id = [n for n in range(size)]

    def __str__(self):
        # Return list
        return str(self.id)

    def root(self, i):
        # Chase parent pointers until reaching root
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        # Determine if p and q are connected
        # O(n)
        return self.root(p) == self.root(q)

    def union(self, p, q):
        # Connect two nodes
        # O(n)
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j

if __name__ == '__main__':
    qf = QuickUnion(10)
    print(qf)
    qf.union(4, 3)
    print(qf)
    qf.union(3, 8)
    print(qf)
    qf.union(6, 5)
    print(qf)
    qf.union(9, 4)
    print(qf)
    qf.union(2, 1)
    print(qf)
    print(qf.connected(8, 9))
    print(qf.connected(5, 0))
    qf.union(5, 0)
    print(qf)
    qf.union(7, 2)
    print(qf)
    qf.union(6, 1)
    print(qf)
    qf.union(7, 3)
    print(qf)
