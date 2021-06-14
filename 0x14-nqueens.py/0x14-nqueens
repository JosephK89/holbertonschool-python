#!/usr/bin/python3
"""
queens
"""


from sys import argv, exit

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    x = argv([1])
    if type(x) is not int:
        print("N must be a number")
        exit(1)
    if x < 4:
        print("N must be at least 4")
        exit(1)
    sol = []
    def board(row, x, sol):
        if row == x:
            print(sol)
        else:
            for col in range(x):
                point = [row, col]
                if issafe(sol, point):
                    sol.append(point)
                    board(row + 1, n, sol)
                    sol.remove(point)
    def issafe(sol, point):
        for queen in sol:
            if queen[1] == point[1]:
                return False
            if queen[0] + queen[1] == point[0] + point[1]:
                return False
            if queen[0] - queen[1] == point[0] - point[1]:
                return False
        return True
    queens(0, n, sol)
