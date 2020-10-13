'''
16.6 Smallest Difference: Given two arrays of integers, compute the pair of values (one value in each
array) with the smallest (non-negative) difference. Return the difference
'''

import numpy  as np
def smallest_diff(a1,a2):
    a1=sorted(a1)
    a2= sorted(a2)

    ind1 =0
    ind2 =0
    diff = np.inf
    pr= []
    while ind1<len(a1) and ind2 <len(a2):
        if abs(a1[ind1] - a2[ind2]) < diff:
            diff = abs(a1[ind1] - a2[ind2])
            pr = [a1[ind1], a2[ind2]]
        if a1[ind1] > a2[ind2]:
            ind2+=1

        else:
            ind1+=1

    return pr

a1 = [1, 3, 15, 11, 2]
a2 = [23, 127, 235, 19, 8]
print(smallest_diff(a1,a2))