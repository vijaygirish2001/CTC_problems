
def is_valid(row,col):
    if row <0 or col<0 or row>2 or col>2:
        return False
    else:
        return True

arr  = [['N' for i in range(3)] for j in range(3)]

print(arr)

no_turns = 0
turn = 0
seen  =  []
while no_turns < 9:

    if turn == 0:
        inp = input('Enter the position for player X')
        row, col = [int(i) for i in  inp.split()]

        while (row,col)  in seen or is_valid(row,col) == False:
            print(' Invalid input ')
            inp = input('Enter the position for player X')
            row, col = [int(i) for i in inp.split()]

        arr[row][col] = 'X'
        m = 'X'
    else:
        inp = input('Enter the position for player O')
        row, col = [int(i) for i in inp.split()]
        while (row, col) in seen or is_valid(row, col) == False:
            print(' Invalid input ')
            inp = input('Enter the position for player O')
            row, col = [int(i) for i in inp.split()]

        arr[row][col] = 'O'
        m= 'O'

    noXrow = 0
    noOrow = 0
    noXcol = 0
    noOcol = 0

    for i in range(3):
        if arr[i][col] == 'X':
            noXrow +=1
        if arr[i][col] == 'O':
            noOrow += 1

    for i in range(3):
        if arr[row][i] == 'X' :
            noXcol +=1
        if arr[row][i] == 'O':
            noOcol += 1

    if noXrow == 3 or noXcol == 3:
        print('X has won')
        break

    if noOrow == 3 or noOcol == 3:
        print('O has won')
        break

    if noXrow + noOrow == 3 or noXcol + noOcol == 3:
        print('Draw')
        break


    turn = 1-turn

    seen.append((row,col))

    for i in range(3):
        print(arr[i])

    no_turns += 1


for i in range(3):
    print(arr[i])


    def restoreIpAddresses(self, A):

        # Place dots
        ind = 1
        B = []
        for ind in range(1, len(A) - 3):
            for ind1 in range(ind + 1, len(A) - 2):
                for ind2 in range(ind1 + 1, len(A) - 1):
                    if (A[0] != '0' and int(A[:ind]) != 0) and (int(A[:ind]) <= 255 and int(A[:ind]) >= 0) and (
                            A[ind] != '0' and int(A[ind:ind1]) != 0) and (
                            int(A[ind:ind1]) <= 255 and int(A[ind:ind1]) >= 0) and (
                            A[ind1] != '0' and int(A[ind1:ind2]) != 0) and (
                            int(A[ind1:ind2]) <= 255 and int(A[ind1:ind2]) >= 0) and (
                            A[ind2] != '0' and int(A[ind2:]) != 0) and (int(A[ind2:]) <= 255 and int(A[ind2:]) >= 0):
                        B.append(A[:ind] + '.' + A[ind:ind1] + '.' + A[ind1:ind2] + '.' + A[ind2:])

        return B



