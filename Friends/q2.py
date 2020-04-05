'''

   Given a list of date intervals, rearrange by removing overlapping intervals
e.g.
2020-01-01 to 2020-01-20
2020-01-15 to 2020-01-29
2020-01-23 to 2020-02-01
'''

import numpy as np
def convert_ranges(date_range):
    lst= []
    d_strt_end = []
    for i in date_range:
        lst.append(i[0])
        d_strt_end.append(0)
        lst.append(i[1])
        d_strt_end.append(1)

    lst_ind = np.argsort(lst)
    ind =0
    fin_lst = []
    while ind<len(lst_ind)-1:
        if lst[lst_ind[ind]] < lst[lst_ind[ind+1]]:
            if d_strt_end[lst_ind[ind]] == 0 and d_strt_end[lst_ind[ind+1]]==1:
                fin_lst.append([lst[lst_ind[ind]],lst[lst_ind[ind+1]] ])
                ind+=1
            elif d_strt_end[lst_ind[ind]] == 1 and d_strt_end[lst_ind[ind+1]]==1:
                fin_lst.append([lst[lst_ind[ind]]+1, lst[lst_ind[ind + 1]]])
                ind += 1
            elif d_strt_end[lst_ind[ind]] == 0 and d_strt_end[lst_ind[ind+1]]==0:
                fin_lst.append([lst[lst_ind[ind]] , lst[lst_ind[ind + 1]]-1])
                ind += 1
            else:
                ind+=1
        elif lst[lst_ind[ind]] == lst[lst_ind[ind+1]]:
            if d_strt_end[lst_ind[ind]] == 1 and d_strt_end[lst_ind[ind+1]]==0:
                fin_lst.pop()
                fin_lst.append([lst[lst_ind[ind-1]],lst[lst_ind[ind]]-1 ])

            ind+=1




    return fin_lst

a = [[3,6],[3,5], [15,29],[23,32], [40,45]]
print(convert_ranges(a))


def splitIntervals(inv):
    output = []
    modify = [x - 1 for x, _ in inv]
    modify.extend([y for _, y in inv])
    modify = sorted(np.unique(modify))
    print(modify)

    i = 0
    N = len(modify)
    while i < N - 1:
        prev = modify[i] + 1
        i += 1
        curr = modify[i]
        for start, end in inv:
            if prev >= start and prev <= end and curr >= start and curr <= end:
                output.append((prev, curr))
                break
    return output


print(splitIntervals(a))






    #fin_range.append((lst[ind], lst[ind + 1] - 1))

