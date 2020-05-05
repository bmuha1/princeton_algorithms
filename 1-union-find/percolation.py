#!/usr/bin/python3
# Estimate the value of the percolation threshold via Monte Carlo simulation
from weighted_quick_union_path_compression import WeightedQuickUnionPathComp


class Percolation:
    # Model a percolation system
    def __init__(self, n):
        # Create n-by-n grid, with all sites initially blocked
        if n <= 0:
            raise Exception('N should be larger than 0')
        self.grid = [[1 for i in range(n)] for j in range(n)]
        self.size = n
        self.u = WeightedQuickUnionPathComp(n ** 2 + 2)
        for i in range(n):
            self.u.union(n ** 2, i)
            self.u.union(n ** 2 + 1, n * (n - 1) + i)

    def __str__(self):
        # Print the grid
        grid = ''
        for row in self.grid:
            for col in row:
                if col == 1:
                    grid += 'X'
                else:
                    grid += ' '
            grid += '\n'
        return grid[:-1]

    def open(self, row, col):
        # Open the site if it's not already open
        if row < 1 or col < 1 or row > len(self.grid) or col > len(self.grid):
            raise Exception('Coordinate is outside the grid range')
        row -= 1
        col -= 1
        if self.grid[row][col]:
            self.grid[row][col] = 0
            if col + 1 < self.size and self.grid[row][col + 1] == 0:
                self.u.union(row * self.size + col, row * self.size + col + 1)
            if col - 1 >= 0 and self.grid[row][col - 1] == 0:
                self.u.union(row * self.size + col, row * self.size + col - 1)
            if row + 1 < self.size and self.grid[row + 1][col] == 0:
                self.u.union(row * self.size + col,
                             (row + 1) * self.size + col)
            if row - 1 >= 0 and self.grid[row - 1][col] == 0:
                self.u.union(row * self.size + col,
                             (row - 1) * self.size + col)

    def is_open(self, row, col):
        # Check if the site is open
        if row < 1 or col < 1 or row > len(self.grid) or col > len(self.grid):
            raise Exception('Coordinate is outside the grid range')
        return self.grid[row - 1][col - 1] == 0

    def is_full(self, row, col):
        # Check if the site is full
        if row < 1 or col < 1 or row > len(self.grid) or col > len(self.grid):
            raise Exception('Coordinate is outside the grid range')
        else:
            return self.grid[row - 1][col - 1] == 1

    def number_open_sites(self):
        # Return the number of open sites
        count = 0
        for row in self.grid:
            for col in row:
                if col == 0:
                    count += 1
        return count

    def percolates(self):
        # Check if the system percolates
        return self.u.root(self.size ** 2) == self.u.root(self.size ** 2 + 1)

if __name__ == '__main__':
    p = Percolation(5)
    print(p)
    print(p.percolates())
    print('-----')

    p.open(2, 2)
    print(p)
    print(p.percolates())
    print('-----')

    p.open(1, 2)
    print(p)
    print(p.percolates())
    print('-----')

    p.open(3, 1)
    print(p)
    print(p.percolates())
    print('-----')

    p.open(4, 1)
    print(p)
    print(p.percolates())
    print('-----')

    p.open(4, 2)
    print(p)
    print(p.percolates())
    print('-----')

    p.open(4, 3)
    print(p)
    print(p.percolates())
    print('-----')

    p.open(4, 4)
    print(p)
    print(p.percolates())
    print('-----')

    p.open(5, 4)
    print(p)
    print(p.percolates())
    print('-----')

    p.open(2, 1)
    print(p)
    print(p.percolates())
    print('-----')
