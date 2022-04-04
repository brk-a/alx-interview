#!/usr/bin/python3

'''
a function `pascal_triangle(n)` that 
returns a list of lists of integers representing
the Pascal’s triangle of size n

'''

def pascal_triangle(n):
    ''' pascal's triangle '''
    n = n if n and isinstance(n, int) else None
    result = []
    if not n:
        return result
    
