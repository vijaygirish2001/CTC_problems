'''
oomsday Fuel
=============

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel.

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly.
'''



from fractions import Fraction
def solution(m):
    def transposeMatrix(m):
        return map(list, zip(*m))

    def getMatrixMinor(m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    def getMatrixDeternminant(m):
        # base case for 2x2 matrix
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]

        determinant = 0
        for c in range(len(m)):
            determinant += ((-1) ** c) * m[0][c] * getMatrixDeternminant(getMatrixMinor(m, 0, c))
        return determinant

    def getMatrixInverse(m):
        determinant = getMatrixDeternminant(m)
        # special case for 2x2 matrix:
        if len(m) == 2:
            return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                    [-1 * m[1][0] / determinant, m[0][0] / determinant]]

        # find matrix of cofactors
        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = getMatrixMinor(m, r, c)
                cofactorRow.append(((-1) ** (r + c)) * getMatrixDeternminant(minor))
            cofactors.append(cofactorRow)
        cofactors = transposeMatrix(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c] / determinant
        return cofactors
    def gcd(x, y):
        def gcd1(x, y):
            if y == 0:
                return x
            return gcd1(y, x % y)

        return gcd1(abs(x), abs(y))
    def lcm(x, y):
        return long(x * y / gcd(x, y))

    ind= 0
    terminal_id = []

    Q_R = []



    for row in m:
        sm = float(sum(row))
        if sm == 0:
            terminal_id.append(ind)
        else:
            for colid, val in enumerate(row):
                m[ind][colid] = float(m[ind][colid])/sm

            Q_R.append(m[ind])

        ind+=1

    if not Q_R:
        return [1]*(len(terminal_id)+1)
    Q = []
    R = []
    for row in Q_R:
        tmp_Q = []
        tmp_R = []
        for ind, val in enumerate(row):
            if ind not in terminal_id:
                tmp_Q.append(val)
            else:
                tmp_R.append(val)

        Q.append(tmp_Q)
        R.append(tmp_R)

    l = len(Q)

    for i in range(l):
        for j in range(l):
            if i == j:
                Q[i][j] = 1 - Q[i][j]
            else:
                Q[i][j] = - Q[i][j]

    Qinv = getMatrixInverse(Q)

    no_col= len(R[0])
    term_num = []
    term_den = []
    for i in range(no_col):
        tmp = 0
        for j in range(len(Qinv[0])):
            tmp += Qinv[0][j] * R[j][i]
        tmp_frac = Fraction(tmp).limit_denominator()
        term_num.append(tmp_frac.numerator)
        term_den.append(tmp_frac.denominator)

    fin_dem = 1
    ind = 0
    while ind < len(term_den):
        if term_den[ind] > 0:
            fin_dem = lcm(fin_dem,term_den[ind])
        ind+=1

    ind = 0
    fin_prob = []
    while ind < len(term_num):
        fin_prob.append(int(fin_dem/term_den[ind] * term_num[ind]))
        ind+=1

    fin_prob.append(int(fin_dem))


    return fin_prob



def solution(m):
    from fractions import Fraction

    def transposeMatrix(m):
        return map(list, zip(*m))

    def getMinor(m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    def getDeterminant(m):
        if len(m)==1:
            return m[0][0]
        if len(m)==2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        determinant = 0
        for c in range(len(m)):
            determinant += ((-1) ** c) * m[0][c] * getDeterminant(getMinor(m, 0, c))
        return determinant

    def getMatrixInverse(m):
        determinant = getDeterminant(m)
        # special case for 2x2 matrix:
        if len(m) == 2:
            return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                    [-1 * m[1][0] / determinant, m[0][0] / determinant]]
        # find matrix of cofactors
        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = getMinor(m, r, c)
                cofactorRow.append(((-1) ** (r + c)) * getDeterminant(minor))
            cofactors.append(cofactorRow)
        cofactors = transposeMatrix(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c] / determinant
        return cofactors

    def find_2lcm(num1, num2):
        if (num1 > num2):
            num = num1
            den = num2
        else:
            num = num2
            den = num1
        rem = num % den
        while (rem != 0):
            num = den
            den = rem
            rem = num % den
        gcd = den
        lcm = int(int(num1 * num2) / int(gcd))
        return lcm

    def find_lcm(l):
        num1 = l[0]
        num2 = l[1]
        lcm = find_2lcm(num1, num2)
        for i in range(2, len(l)):
            lcm = find_2lcm(lcm, l[i])
        return lcm

    def split(oldMat):
        n = len(oldMat)
        mat = oldMat
        for i in range(n):
            weight = sum(oldMat[i])

        nonEndStates = [ i for i,row in enumerate(mat) if sum(row)!=0 ]
        endStates = [ i for i,row in enumerate(mat) if sum(row)==0 ]

        R = [ [ Fraction(0) for _ in range(len(endStates)) ] for _ in range(len(nonEndStates)) ]
        Q = [ [ Fraction(0) for _ in range(len(nonEndStates)) ] for _ in range(len(nonEndStates)) ]
        for i in range(len(nonEndStates)):
            weight = sum(oldMat[nonEndStates[i]])
            for j in range(len(endStates)):
                R[i][j] = Fraction(mat[nonEndStates[i]][endStates[j]],weight)
            for k in range(len(nonEndStates)):
                Q[i][k] = Fraction(mat[nonEndStates[i]][nonEndStates[k]],weight)
        return R,Q

    R,Q = split(m)
    I = [ [ Fraction(1 if i==j else 0) for j in range(len(Q)) ] for i in range(len(Q)) ]
    #T=I-Q
    T = [ [ i-q for i,q in zip(irow,qrow) ] for irow,qrow in zip(I,Q) ]
    #Tinv
    Tinv = getMatrixInverse(T)

    lenTinv = len(Tinv)
    lenMR = len(R)
    lenNR = len(R[0])

    res = [ [ Fraction(0) for _ in range(lenNR) ] for _ in range(lenTinv) ]
    for i in range(lenTinv):
        for j in range(lenNR):
            res[i][j] = sum( Tinv[i][k]*R[k][j] for k in range(lenMR) )

    lcm = find_lcm(list(v.denominator for v in res[0]))
    finalRes = [ int(v.numerator*lcm/v.denominator) for v in res[0] ]
    finalRes.append(lcm)
    return finalRes



m =[
        [0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
        [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
        [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
        [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
print(solution(m))



