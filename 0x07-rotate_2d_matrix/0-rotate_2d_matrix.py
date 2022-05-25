#!/usr/bin/python3

'''
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
'''

def rotate_2d_matrix(matrix):
    """rotate a 2d matrix in-place"""
    rotated = []

    for i in range(len(matrix)):
        for j in range(len(matrix)-1, -1, -1):
            rotated.append(matrix[j][i])

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = rotated.pop(0)


if __name__ == '__main__':
    rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    print('Input matrix:\n {}'.format(matrix))
    rotate_2d_matrix(matrix)
    print('Output matrix:\n {}'.format(matrix))
