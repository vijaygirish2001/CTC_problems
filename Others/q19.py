
# Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

def combine( A, B):
    seq = list(range(1 , A +1))
    comb = []

    lst = [0]*B
    def recur_comb(seq, lst, strt,  A, index):
        if index ==B:
            comb.append([i for i in lst])
            return
        if len(lst) > B:
            return
        i = strt
        while i< A and A-i+1>B-index:
            lst[index] = seq[i]
            recur_comb(seq, lst, i+1,  A, index+1)
           # lst = []
            i += 1

        return

    def recur_comb2(seq, lst, i,  A, index):
        if index ==B:
            comb.append([i for i in lst])
            return
        if i>A:
            return

        lst[index] = seq[i]
        recur_comb(seq, lst, i+1,  A, index+1)

        recur_comb(seq, lst, i + 1, A, index )

        return

    recur_comb2(seq, lst, 0,  A, 0)

    return sorted(comb)


print(combine(3,2))