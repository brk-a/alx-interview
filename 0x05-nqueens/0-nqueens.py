#!/usr/bin/python3

'''
The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard. Write a program that solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number of arguments,
print Usage: nqueens N, followed by a new line, and exit with the
status 1
N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by a new
line, and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a new
line, and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don’t have to print the solutions in a specific order
You are only allowed to import the sys module
'''

import sys


def print_board(board, n):
    """prints allocated positions to the queen"""
    b = []

    for i in range(n):
        for j in range(n):
            if j == board[i]:
                b.append([i, j])
    print(b)


def safe_position(board, i, j, r):
    """Determines whether the position is safe for the queen"""
    if (board[i] == j) or (board[i] == j - i + r) or (board[i] == i - r + j):
        return True
    return False


def determine_positions(board, row, n):
    """Recursively finds all safe positions where the queen can be allocated"""
    if row == n:
        print_board(board, n)

    else:
        for j in range(n):
            allowed = True
            for i in range(row):
                if safe_position(board, i, j, row):
                    allowed = False
            if allowed:
                board[row] = j
                determine_positions(board, row + 1, n)


def create_board(size):
    """Generates the board"""
    return [0 * size for i in range(size)]


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except BaseException:
    print("N must be a number")
    exit(1)

if (n < 4):
    print("N must be at least 4")
    exit(1)

board = create_board(int(n))
row = 0
determine_positions(board, row, int(n))


if __name__ == '__main__':
    print('nqueens: N = 4:')
    determine_positions(8, 0, 4)
    print('nqueens: N = 6:')
    determine_positions(8, 0, 6)
