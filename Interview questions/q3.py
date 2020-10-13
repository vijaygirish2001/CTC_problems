def numOffices( grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    # your code here
    m = len(grid)
    n1= len(grid[0])
    office = {}
    n = 0

    for i in range(m):
        for j in range(n1):
            print(i, j)
            if grid[i][j] == 1:
                fnd = 0
                if office:
                    for k in office:
                        if (i - 1, j) in office[k] or (i, j - 1) in office[k]:
                            fnd = 1
                            office[k].append((i, j))
                            break
                    if fnd == 0:
                        office[n] = [(i, j)]
                        n += 1

                else:
                    print(1)
                    office[n] = [(i, j)]
                    n += 1

    return n

grid =[[1,1],[1,0]]

print((numOffices( grid)))