'''
A 2d array has 0 and 1 as values. In one flip, 0's are changed to 1 if and only if any of the neighbors (left, right, top, bottom) is 1.
 Return the total number of flips required to convert the whole grid to 1's

'''
from collections import deque
valid_dir = [[1,0],[0,1],[-1,0],[0,-1]]

def noflips(arr):
    if not arr:
        return 0
    m =len(arr)
    n = len(arr[0])

    b = deque()
    seen = dict()

    def is_element(i,j):
        if i>=0 and j>=0 and i<m and j<n:
            return True
        return False

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                seen[(i,j)] = 0
                b.append((i,j))

    while b:
        i,j = b.pop()
        for d in valid_dir:
            ii = i +d[0]
            jj = j +d[1]
            if is_element(ii,jj) and not arr[ii][jj] and (ii,jj) not in seen:
                seen[(ii,jj)] = seen[(i,j)]+1
                b.append((ii,jj))

    if seen:
        return max(seen.values())
    else:
        return -1



a = [[0, 0,1],
     [0, 0,0],
    ]
print(noflips(a))





