'''
Eight Queens:Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
diagonals, not just the two that bisect the board.
'''


queen_placements = []
sz = 8

def check_valid(row,col, col_dict):

    for i in range(row):
        try:
            if col_dict[i] == col:
                return False
            if abs(row-i) == abs(col- col_dict[i]):
                return False
        except:
            pass

    return True

def place_queen(row, col_dict):


    if row >=sz:
        return col_dict
    for col in range(sz):
        if check_valid(row,col, col_dict):
            col_dict[row] = col

            col_dict = place_queen(row+1, col_dict)

    return col_dict

col_dict = place_queen(0, dict())

print(col_dict)

