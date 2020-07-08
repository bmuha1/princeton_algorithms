#!/usr/bin/python3
# Solve the 8-puzzle problem using the A* search algorithm
from copy import deepcopy


class Board:
    # 8-puzzle board
    def __init__(self, n, tiles):
        # Initialize board
        self.tiles = [[0] * n for _ in range(n)]
        self.size = n
        y = x = 0
        for i in tiles:
            self.tiles[y][x] = i
            x += 1
            if x == n:
                y, x = y + 1, 0

    def __str__(self):
        # Print the board size n, followed by the grid
        # 0 designates the blank square
        s = str(self.size) + '\n'
        for y in range(self.size):
            for x in range(self.size):
                s += ' ' + str(self.tiles[y][x])
            s += '\n'
        return s

    def __eq__(self, other):
        # Two boards are equal if they have the same size and their
        # corresponding tiles are in the same positions
        return self.size == other.size and self.tiles == other.tiles

    def dimension(self):
        # Return the board dimension n
        return self.size

    def hamming(self):
        # Return the number of tiles out of place
        tiles, current = 0, 1
        for y in range(self.size):
            for x in range(self.size):
                if self.tiles[y][x] != current and current < self.size ** 2:
                    tiles += 1
                current += 1
        return tiles

    def manhattan(self):
        # Return the sum of the Manhattan distances (sum of the vertical and
        # horizontal distance) between tiles and goal
        goal, actual = {}, {}
        current, y, x = 1, 0, 0
        while current <= self.size ** 2:
            goal[current] = [y, x]
            actual[self.tiles[y][x]] = [y, x]
            x += 1
            if x == self.size:
                y, x = y + 1, 0
            current += 1

        distance = 0
        for i in range(1, self.size ** 2):
            distance += abs(goal[i][0] - actual[i][0])
            distance += abs(goal[i][1] - actual[i][1])
        return distance

    def neighbors(self):
        # Return all neighboring boards
        neighbors = []
        for y in range(self.size):
            for x in range(self.size):
                if self.tiles[y][x] == 0:
                    y0, x0 = y, x
        if y0 > 0:
            temp = deepcopy(self.tiles)
            temp[y0][x0], temp[y0 - 1][x0] = temp[y0 - 1][x0], temp[y0][x0]
            neighbors.append(temp)
        if x0 > 0:
            temp = deepcopy(self.tiles)
            temp[y0][x0], temp[y0][x0 - 1] = temp[y0][x0 - 1], temp[y0][x0]
            neighbors.append(temp)
        if y0 < self.size - 1:
            temp = deepcopy(self.tiles)
            temp[y0][x0], temp[y0 + 1][x0] = temp[y0 + 1][x0], temp[y0][x0]
            neighbors.append(temp)
        if x0 < self.size - 1:
            temp = deepcopy(self.tiles)
            temp[y0][x0], temp[y0][x0 + 1] = temp[y0][x0 + 1], temp[y0][x0]
            neighbors.append(temp)
        return neighbors


if __name__ == '__main__':
    board = Board(3, [0, 1, 3, 4, 2, 5, 7, 8, 6])
    board2 = Board(3, [8, 1, 3, 4, 0, 2, 7, 6, 5])
    board3 = Board(3, [8, 1, 3, 4, 0, 2, 7, 6, 5])

    print(board)
    print('hamming:', board.hamming())
    print('manhattan:', board.manhattan())
    print(board2)
    print('hamming:', board2.hamming())
    print('manhattan:', board2.manhattan())

    print('equal:', board == board2)
    print('equal:', board2 == board3)

    print(board.neighbors())
    print(board2.neighbors())
