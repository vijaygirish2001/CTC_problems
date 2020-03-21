'''
Permutations with Duplicates: Write a method to compute all permutations of a string whose
characters are not necessarily unique. The list of permutations should not have duplicates.
'''

def perms_all(wrds_occ, remaining, prefix, result):
    if remaining == 0:
        result.append(prefix)
        return

    for i in wrds_occ:
        c=wrds_occ[i]
        if c>0:
            wrds_occ[i] = c-1
            print(prefix, i, result)
            perms_all(wrds_occ, remaining-1, prefix+i, result)
            wrds_occ[i] = c


a='cntc'

def perms_dup(a):
    wrds_occ =dict()
    for i in a:
        if i in wrds_occ:
            wrds_occ[i] += 1
        else:
            wrds_occ[i] = 1
    result = []
    perms_all( wrds_occ, len(a),'', result)

    print(wrds_occ, result)


perms_dup(a)