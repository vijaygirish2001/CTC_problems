# NQueens

def solveNQueens( A):
    col, diag1, diag2 = [False] * A, [False] * (2 * A), [False] * (2 * A)
    row, res = [], []

    def trace(i):
        if i == A:
            res.append([])
            for j in row:
                res[-1].append('.' * (j) + 'Q' + '.' * (A - j - 1))
                print(row,res[-1])
        for j in range(A):
            if not (col[j] or diag1[i + j] or diag2[i - j + A]):
                col[j] = diag1[i + j] = diag2[i - j + A] = True;
                row.append(j)
                trace(i + 1)
                col[j] = diag1[i + j] = diag2[i - j + A] = False;
                row.pop()

    trace(0)
    return res


print(solveNQueens( 5))