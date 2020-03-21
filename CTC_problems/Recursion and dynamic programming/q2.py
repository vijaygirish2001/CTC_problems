'''
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right

'''

seen = []
def find_pth(r,c,off_lim,y,x,pth):
    if y>r or x>c or (y,x) in off_lim+seen:
        pth= []
        return pth
    pth.append((y , x))
    seen.append((y, x))
    if pth[-1][0] == r and pth[-1][1] == c:
        return pth




    if find_pth(r, c, off_lim, y+1,x, pth) or find_pth(r, c, off_lim, y,x+1, pth) :
        return pth
    return False

print(find_pth(3,3,[(2,1)],1,1,[] ))


