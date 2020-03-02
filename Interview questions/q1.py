# Find the minimum path between (x1,y1) and (x2,y2)
import numpy as np


def min_path(is_possible, x1, y1, x2, y2):
    dist_min = np.ones((is_possible.shape)) * np.inf

    if x1 == x2 and y1 == y2:
        return 0

    dist_min[x1, y1] = 0

    i = x1
    while i <= x2:
        j = y1
        while j >= y2:
            if i + 1 <= x2 and is_possible[i + 1, j] == 1:
                dist_min[i + 1, j] = min(dist_min[i + 1, j], dist_min[i, j] + 1)
            if j - 1 >= 0 and is_possible[i, j - 1] == 1:
                dist_min[i, j - 1] = min(dist_min[i, j - 1], dist_min[i, j] + 1)
            if i + 1 <= x2 and j - 1 >= 0 and is_possible[i + 1, j - 1] == 1:
                dist_min[i + 1, j - 1] = min(dist_min[i + 1, j - 1], dist_min[i, j] + 1)

            j -= 1
        i += 1

    return dist_min[x2, y2]



is_possible = np.ones((3,3))
is_possible[1,1]=0
is_possible[1,2]=1

dist_min =min_path(is_possible, 0, 2, 2, 0)

print(dist_min)