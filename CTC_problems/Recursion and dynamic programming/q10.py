'''
8.10 Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
fill in the surrounding area until the color changes from the original color.

'''

import numpy as np


def color_fill(A, i, j):
    if i >= A.shape[0] or j >= A.shape[1] or i < 0 or j < 0:
        return
    print(i,j)
    if A[i, j] == 0:
        A[i, j] = 1

        color_fill(A, i + 1, j)
        color_fill(A, i - 1, j)
        color_fill(A, i, j + 1)
        color_fill(A, i, j - 1)

    return A


# Using bfs
def color_fill_bfs(A, i, j):
    lst = []
    lst.append((i,j))
    visited = []
    while lst:
        m = lst.pop(0)
        if m in visited:
            continue
        i,j = m
        print(m)
        visited.append(m)
        if A[m[0], m[1]] == 0:
            A[m[0], m[1]] = 1
        if i+1< A.shape[0]:
            lst.append((i+1,j))


        if j+1< A.shape[1]:
            lst.append((i,j+1))

        if i - 1 >=0:
            lst.append((i - 1, j))

        if j - 1 >=0:
            lst.append((i, j - 1))

    return A

A = np.zeros((10, 12))

A = color_fill(A, 0, 0)

print(A)
