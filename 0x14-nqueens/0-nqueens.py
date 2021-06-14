#!/usr/bin/python3
""""
queens module
"""

from sys import argv, exit

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
    except BaseException:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    sol = []

    def queens(row, n, sol):
        if row == n:
            print(sol)
        else:
            for col in range(n):
                placement = [row, col]
                if issafe(sol, placement):
                    sol.append(placement)
                    queens(row + 1, n, sol)
                    sol.remove(placement)

    def issafe(sol, placement):
        for queen in sol:
            if queen[1] == placement[1]:
                return False
            if queen[0] + queen[1] == placement[0] + placement[1]:
                return False
            if queen[0] - queen[1] == placement[0] - placement[1]:
                return False
        return True

    solve_queens(0, n, sol)
