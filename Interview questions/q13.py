'''
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, but once they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions.

You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1).

Write a function solution(map) that generates the length of the shortest path from the prison door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
Output:
    7
'''

# BFS
def solution(map):
    # Your code here
    h = len(map)
    w = len(map[0])

    def is_valid(y,x):
        if y>=0 and y<h and x>=0 and x<w:
            return True
        else:
            return False

    def chk_blk_node(nxt_node, tot_depth_1, tot_depth):
        for block_node in [[nxt_node[0] + 1, nxt_node[1]], [nxt_node[0], nxt_node[1] + 1],
                           [nxt_node[0] - 1, nxt_node[1]],
                           [nxt_node[0], nxt_node[1] - 1]]:
            if is_valid(block_node[0], block_node[1]) and map[block_node[0]][block_node[1]] == 1:
                ind_blk = str(block_node[0]) + str(block_node[1])
                if ind_blk in tot_depth_1:
                    tot_depth_1[ind_blk] = min(tot_depth_1[ind_blk], tot_depth[str(nxt_node[0]) + str(nxt_node[1])])
                else:
                    tot_depth_1[ind_blk] = tot_depth[str(nxt_node[0]) + str(nxt_node[1])]

        return tot_depth_1

    def bfs(strt, map):
        tot_depth = {}
        is_visit = []
        tot_depth[str(strt[0]) + str(strt[1])] = 1
        tot_depth_1 = {}
        seen = [strt]
        tot_depth_1 = chk_blk_node(strt, tot_depth_1, tot_depth)

        while seen:
            node = seen.pop(0)
            if node not in is_visit:
                is_visit.append(node)
                for nxt_node in [[node[0] + 1, node[1]], [node[0], node[1] + 1], [node[0] - 1, node[1]],
                                 [node[0], node[1] - 1]]:
                    if is_valid(nxt_node[0], nxt_node[1]):
                        if map[nxt_node[0]][nxt_node[1]] == 0:
                            tot_depth[str(nxt_node[0]) + str(nxt_node[1])] = tot_depth[str(node[0]) + str(node[1])] + 1
                            seen.append(nxt_node)
                            tot_depth_1 = chk_blk_node(nxt_node, tot_depth_1, tot_depth)


        return tot_depth, tot_depth_1

    strt = [0,0]

    tot_depth, tot_depth_1 = bfs(strt,map)
    strt = [h-1, w-1]
    tot_depth_rev, tot_depth_rev_1 = bfs(strt, map)
    min_depth = float('inf')
    for ind in tot_depth_1:
        if ind in tot_depth_rev_1:
            min_depth = min(min_depth, tot_depth_1[ind] + tot_depth_rev_1[ind] +1)

    if str(h-1) + str(w-1) in tot_depth:
        min_depth = min(min_depth, tot_depth[str(h-1) + str(w-1)])
    return min_depth


'''
def solution(map):
    # Your code here
    h = len(map)
    w = len(map[0])

    min_pth_0 = [[float('inf') for i in range(w)] for j in range(h)]
    min_pth_1 = [[float('inf') for i in range(w)] for j in range(h)]

    min_pth_0[0][0] = 1
    #min_pth_1[0][0] = 1
    def is_valid(y, x):
        if y >= 0 and y < h and x >= 0 and x < w:
            return True
        else:
            return False

    for i in range(h):
        for j in range(w):
            for nxt in [(1,0),(0,1),(-1,0),(0,-1)]:
                if is_valid(i+nxt[0], j+nxt[1]):
                    if map[i+nxt[0]][j+nxt[1]] == 1:
                        min_pth_1[i + nxt[0]][j + nxt[1]] = min(min_pth_1[i + nxt[0]][j + nxt[1]],min_pth_0[i][j] + 1)
                    else:
                        min_pth_0[i + nxt[0]][j + nxt[1]] = min(min_pth_0[i + nxt[0]][j + nxt[1]],min_pth_0[i][j] + 1)
                        min_pth_1[i + nxt[0]][j + nxt[1]] = min(min_pth_1[i + nxt[0]][j + nxt[1]],min_pth_1[i][j] + 1)

    print(min_pth_0)
    return min(min_pth_0[h-1][w-1], min_pth_1[h-1][w-1])


'''








a  = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

print(solution(a))

