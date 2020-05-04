#!/usr/bin/python3
# Implement weighted quick union with path compression


class WeightedQuickUnionPathComp():
    def __init__(self, size):
        # Initialize list
        # O(n)
        self.id = [n for n in range(size)]
        self.size = [1 for n in range(size)]

    def __str__(self):
        # Return list
        return str(self.id)

    def root(self, i):
        # Chase parent pointers until reaching root
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def connected(self, p, q):
        # Determine if p and q are connected
        # O(log(n))
        return self.root(p) == self.root(q)

    def union(self, p, q):
        # Connect two nodes
        # O(log(n))
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]

if __name__ == '__main__':
    qf = WeightedQuickUnionPathComp(10)
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
