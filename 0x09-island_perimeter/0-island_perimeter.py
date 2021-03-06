#!/usr/bin/python3

'''
Create a function def island_perimeter(grid):
that returns the perimeter of the island described in grid:

grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn’t have “lakes” (water inside that isn’t
connected to the water surrounding the island).
'''


def island_perimeter(grid):
    ''' return perimeter of an island '''
    '''new = []
    for i in grid:
        for j in i:
            if j == 1:
                new.append(j)
                '''
    new = [j for i in  grid for j in i if j == 1]
    perimeter = 2 + 2 * len(new)

    return perimeter


if __name__ == '__main__':
    island_perimeter = __import__('0-island_perimeter').island_perimeter
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
