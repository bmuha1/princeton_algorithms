#!/usr/bin/python3
# Solve the 8-puzzle problem using the A* search algorithm


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

    def dimension(self):
        # Return the board dimension n
        return self.size


if __name__ == '__main__':
    board = Board(3, [0, 1, 3, 4, 2, 5, 7, 8, 6])
    print(board)
