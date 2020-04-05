'''
Given an nxn board. A piece can move in steps of size 1 only in Up,Left,Down and Right. A piece cannot come back on board once it goes out of the board.
Position of a piece is given at co-ordinate x,y.
Number of moves = k

WAP to find the probability that the piece will be on board (nxn) after k moves starting from point (x,y)
E.g.4x4 board, starting point (1,0), k=1

'''

no_valid = 0
no_invalid= 0

def prob_on_board(x,y,k,n, level):
    global no_invalid, no_valid

    if x<n and y<n and x>=0 and y>=0:
        if level == k:
            no_valid+=1
            return
    else:
        no_invalid += 1
        return


    prob_on_board(x+1,y,k,n, level+1)
    prob_on_board(x, y+1, k, n, level+1)
    prob_on_board(x-1, y, k, n, level+1)
    prob_on_board(x, y-1, k, n, level + 1)
    print(no_valid,no_invalid)
    return no_valid/(no_valid+no_invalid)

p= prob_on_board(1,0,2,4, 0)
print(p)