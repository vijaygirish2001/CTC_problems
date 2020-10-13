'''
Look and say sequence
'''

n=10
pres = [1]
i=0
while i < n:
    print(' '.join([str(j) for j in pres]))

    ind = 1
    n_pres = []
    while ind< len(pres)+1:
        n_dig =1
        while ind< len(pres) and pres[ind-1] == pres[ind]:
            ind+=1
            n_dig+=1
        n_pres.extend([n_dig, pres[ind-1]])
        ind+=1
    i+=1
    pres= n_pres

print(' '.join([str(j) for j in pres]))

print('dssdsds')

def isMatch( A, B):
    indA = 0
    indB = 0

    fnd = -1
    while indA < len(A):
        #print(indA, indB, len(A))

        if indB < len(B) and (A[indA] == B[indB] or B[indB] == '.'):

            indA += 1
            indB += 1

        elif indB < len(B) and B[indB] == '*':
            print(indA, indB, len(A))

            prev_chr = B[indB - 1]

            fnd = 1

            while indB < len(B) and (B[indB] == '*' or B[indB] == '.'):
                indB += 1
            indA-=1
            print(indA, indB, len(A))
            while indA < len(A) and indB < len(B) and (A[indA] == prev_chr or prev_chr == '.'):
                if A[indA] == B[indB]:
                    indA += 1
                    indB += 1
                    break
                indA +=1

        else:

            if indB + 1 < len(B) and B[indB + 1] == '*':
                indB += 1

            else:

                return 0
    print(indA, indB, len(A),'ds')
    if indB == len(B):
        return 1
    else:
        return 0

A = 'abbc'
B = 'ab*bbc'

print(isMatch( A, B))