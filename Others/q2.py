# Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S

def cont_sub_array(arr,s):
    if sum(arr) < s:
        return None

    lft_ind = 0
    right_ind = 1

    while right_ind<= len(arr) and lft_ind < right_ind:
        sm = sum(arr[lft_ind:right_ind])
        if sm == s:
            return arr[lft_ind:right_ind]
        elif sm >s:
            lft_ind+=1
        else:
            right_ind+=1
    return None

arr = [1,0,3,5,2]

print(cont_sub_array(arr,7))