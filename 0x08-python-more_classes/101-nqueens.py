#!/usr/bin/python3
"""Module contains a class named NQueens
"""


class NQueens:
    def __init__(self, size):
        self.__n = size
        self.__count = 0
        self.__num_of_solutions = 0
        self.__board = [[0] * size for _ in range(size)]
        self.__solution = []

    def __is_valid(self, row, col):
        """
        Checks if the current position on the board is ok
        """
        for i in range(row):
            """
            Check if another queen is on the current column
            """
            if self.__board[i][col] == 1:
                return False

        """
        Check if a queen is on the same diagonal as the current position
        """
        """
        First check the diagonal on the left of the current position
        """
        for i, j in zip(list(range(row, -1, -1)), list(range(col, -1, -1))):
            if self.__board[i][j] == 1:
                return False
            
        """
        Then, check the diagonal on the right of the current position
        """
        for i, j in zip(
                list(range(row, -1, -1)), list(range(col, self.__n, 1))):
            if self.__board[i][j] == 1:
                return False

        """
        If the position is okay, return True
        """
        return True

    def __backtrack(self, row):
        """
        Recursively searches for solutions
        """
        self.__count += 1
        if row == self.__n:
            self.__num_of_solutions += 1
            self.__solution.append([i[:] for i in self.__board])
            return

        for col in range(self.__n):
            if self.__is_valid(row, col):
                self.__board[row][col] = 1
                self.__backtrack(row + 1)
                self.__board[row][col] = 0

    def solve(self):
        if not self.__solution:
            self.__backtrack(0)
        return self.__solution


def print_simpler_solution(solutions):
    """
    prints nqueens solution in a simple format by printing the position of
    a queen which is placed on a row and column
    """
    for solution in solutions:
        new_solution = []
        for row, j in enumerate(solution):
            new_row = []
            for col, k in enumerate(j):
                if k == 1:
                    new_row.append([row, col])
            new_solution.append(new_row)
        print(new_solution)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print('N must be at least 4')
            sys.exit(1)
    except Exception:
        print('N must be a number')
        sys.exit(1)
    print_simpler_solution(NQueens(n).solve())
