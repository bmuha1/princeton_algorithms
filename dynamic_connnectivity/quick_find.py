#!/usr/bin/python3
# Implement quick find


class QuickFind():
    def __init__(self, size):
        # Initialize list
        # O(n)
        self.id = [n for n in range(size)]

    def __str__(self):
        # Return list
        return str(self.id)

    def connected(self, p, q):
        # Determine if p and q are connected
        # O(1)
        return self.id[p] == self.id[q]

    def union(self, p, q):
        # Connect two nodes
        # O(n)
        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid

if __name__ == '__main__':
    qf = QuickFind(10)
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
