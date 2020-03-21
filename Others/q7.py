'''

Given an array of positive and negative integers {-1,6,9,-4,-10,-9,8,8,4} (repetition allowed)
sort the array in a way such that the starting from a positive number, the elements should be arranged as one positive and one negative element maintaining insertion order.
First element should be starting from positive integer and the resultant array should look like {6,-1,9,-4,8,-10,8,-9,4}

'''
def srt_pos_neg(arr):
    arr_pos = []
    arr_neg = []

    for i in arr:
        if i>=0:
            arr_pos.append(i)
        else:
            arr_neg.append(i)

    fin_arr =[]
    ind_alt = 0
    while arr_pos or arr_neg:
        if arr_pos and ind_alt ==0:
            fin_arr.append(arr_pos.pop(0))

        elif arr_neg and ind_alt == 1:
            fin_arr.append(arr_neg.pop(0))
        ind_alt = 1 - ind_alt

    return fin_arr

def srt_pos_neg_no_sep(arr):
    pos_ind = 0
    neg_ind =0
    fin_arr = []
    l= len(arr)
    while len(fin_arr)<l:
        while pos_ind<l and arr[pos_ind]<0:
            pos_ind+=1
        if pos_ind < l:
            fin_arr.append(arr[pos_ind])
            pos_ind+=1

        while neg_ind < l and arr[neg_ind]>=0:
            neg_ind += 1
        if neg_ind < l:
            fin_arr.append(arr[neg_ind])
            neg_ind += 1


    return fin_arr

print(srt_pos_neg_no_sep([-1,2,3,-5,-6,3,8,9,7]))




