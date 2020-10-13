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
    strt_end_dict = {}
    for i in date_range:
        lst.append(i[0])
        d_strt_end.append(0)
        lst.append(i[1])
        d_strt_end.append(1)

        if i[0] in strt_end_dict:
            if i[1]>strt_end_dict[i[0]]:
                strt_end_dict[i[0]] = i[1]
        else:
            strt_end_dict[i[0]] = i[1]

    lst_ind = np.argsort(lst)
    ind =0
    fin_lst = []
    fnd = 0
    while ind<len(lst_ind)-1:
        for i in date_range:
            if lst[lst_ind[ind]] >= i[0] and  lst[lst_ind[ind + 1]] <= i[1]:
                if d_strt_end[lst_ind[ind]] == 0:
                    s = lst[lst_ind[ind]]
                else:
                    s = lst[lst_ind[ind]] +1

                if d_strt_end[lst_ind[ind+1]] == 0:
                    t = lst[lst_ind[ind+1]]-1
                else:
                    t = lst[lst_ind[ind+1]]


                fin_lst.append([s,t])
                ind+=1

                fnd = 1
                break

        if fnd ==0:
            ind += 1
        else:
            fnd = 0





    return fin_lst

a = [[3,12],[5,8],[11,11], [15,29],[23,32], [40,45]]
print(convert_ranges(a))


def splitIntervals(inv):
    output = []
    modify = [x - 1 for x, _ in inv]
    modify.extend([y for _, y in inv if y-1 not in modify])
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

