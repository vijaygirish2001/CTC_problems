def permutelst(x, strt, end):
    if strt == end:
        print(x)

    for j in range(strt,end):
        x[strt], x[j] = x[j], x[strt]
        #print(x,j,strt)
        permutelst(x, strt+1, end)
       # print(x, j,':',strt)
        x[strt], x[j] = x[j], x[strt]


    return


def combs(a):
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c+[a[0]]]
    return cs



x= [1,4,2,6]
print(combs(sorted(x, reverse=True)))