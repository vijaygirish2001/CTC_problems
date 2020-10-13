
'''
Find largest consecutive increasing or decreasing subsequence
'''
import numpy as np
def max_len_arr(lst):
    i = 0
    max_l = 0
    while i< len(lst) - 1:
        loc_l = 1

        sgn = np.sign(lst[i + 1] - lst[i])
        while i+1 < len(lst) and abs(lst[i+1] - lst[i]) == 1 and sgn == np.sign(lst[i + 1] - lst[i]) :

            loc_l += 1
            i += 1

        max_l = max(max_l,loc_l)
        i+=1

    return max_l
aa=[3, 2, 7, 3 ,10, 9,10, 1,2,3 ,4 ,4, 5]
print(max_len_arr([5,6 ,4,5, 6,8,9,10,11,12,13]))