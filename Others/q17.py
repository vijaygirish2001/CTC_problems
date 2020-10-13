# Kth Permutation Sequence

def permute(n):
    a = list(range(1,n+1))

    a = sorted(a)
    def recur_perm(a):
        if len(a) == 0:
            return []
        if len(a) == 1:
            return [a]

        f = []
        for i in range(len(a)):
            m = a[i]
            k = a[:i] +a[i+1:]

            for j in recur_perm(k):
                f.append([m] + j)

        return f
    return recur_perm(a)

n=4
print(permute(n))

import math
def getPermutation( n, k):
    numbers = list(range(1, n + 1))
    permutation = ''
    k -= 1
    while n > 0:
        n -= 1
        # get the index of current digit
        index, k = divmod(k, math.factorial(n))
        print(index,k, math.factorial(n))
        permutation += str(numbers[index])
        # remove handled number
        numbers.remove(numbers[index])
    return permutation



print(getPermutation( 4, 3))


def combinationSum( A, B):
    n = len(A)
    comb = []
    for i in range(1,2**n):
        cmb_i = []
        for j in range(n):
            if 1<<j & i:
                cmb_i.append(A[j])

        if sum(cmb_i) == B:
            comb.append(cmb_i)

    return comb

print(combinationSum( [2,3, 4], 1))







    # no of combinations