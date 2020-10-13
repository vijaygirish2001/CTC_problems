'''
16.19 Pond Sizes: You have an integer matrix representing a plot of land, where the value at that location
represents the height above sea level. A value of zero indicates water. A pond is a region of water
connected vertically, horizontally, or diagonally. The size of the pond is the total number of
connected water cells. Write a method to compute the sizes of all ponds in the matrix.
EXAMPLE
Input:
0 2 1 0
0 1 0 1
1 1 0 1
0 1 0 1
Output: 2, 4, 1 (in any order)
'''

def bfs_pond(arr):

    seen = []
    l =len(arr)
    h  = len(arr[0])
    sz = []
    for i in range(0,l):
        for j in range(0, h):
            if (i,j) not in  seen and arr[i][j] == 0:
                s= 0
                grp = [(i,j)]
                seen.append((i,j))
                while grp:
                    pt = grp.pop(0)
                    s += 1

                    if (pt[0] + 1, pt[1]) not in seen and pt[0] + 1 < l and  arr[pt[0] + 1][pt[1]] == 0:
                        grp.append((pt[0] + 1, pt[1]))
                        seen.append((pt[0] + 1, pt[1]))
                    if (pt[0]+1, pt[1]-1) not in seen and pt[0] + 1 < l and pt[1] - 1>=0 and  arr[pt[0]+1][pt[1]-1] == 0:
                        grp.append((pt[0] +1, pt[1] -1))
                        seen.append((pt[0] +1, pt[1]-1))

                    if (pt[0]+1, pt[1]+1) not in seen and pt[0]+1 <l and pt[1] + 1<h and  arr[pt[0]+1][pt[1]+1] == 0:
                        grp.append((pt[0]+1 , pt[1] +1))
                        seen.append((pt[0]+1, pt[1]+1))

                    if (pt[0], pt[1]+1) not in seen and pt[1] + 1<h and  arr[pt[0]][pt[1]+1] == 0:
                        grp.append((pt[0] , pt[1] +1))
                        seen.append((pt[0], pt[1]+1))
                sz.append(s)

    return sz


arr = [[0, 2, 1 ,0],
[0, 1, 0, 1],
[1, 1, 0, 1],
[0 ,1 ,0 ,1]]


print(bfs_pond(arr))



def dfs_pond(arr, seen):
    def compute(arr, i, j):
        if i < 0 or i >= l or j < 0 or j >= h or (i, j) in seen or arr[i][j]!=0:
            return 0

        s = 1
        seen.append((i, j))
        for m in range(-1, 2):
            for n in range(-1, 2):
                s += compute(arr, i + m, j + n)

        return s
    l = len(arr)
    h = len(arr[0])
    sz = []
    for i in range(0, l):
        for j in range(0, h):
            if (i, j) not in seen and arr[i][j] == 0:
                sz.append(compute(arr, i,j))

    return sz




print(dfs_pond(arr, []))





