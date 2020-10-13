#Kickstart 2020 round E

def longest_arithmetic(arr):
    nmax = 2

    ind = 1

    while ind < len(arr) - 1:
        n = 2
        while ind < len(arr) - 1 and (arr[ind] - arr[ind - 1]) == (arr[ind+1] - arr[ind]):
            n += 1
            ind += 1

        nmax = max(n,nmax)
        ind += 1

    return nmax

a  = '5 4 3 2 1 2 3 4 5 6'.split()
a = [int(i) for i in a]
print(longest_arithmetic(a))


def high_buildings(n, a , b , c):
    no_middle = c
    arr  = [n]*c
    no_left = a - c
    if arr:
        nxt = n-1
    else:
        nxt = n
    if no_left < 0:
        return 'IMPOSSIBLE'
    else:
        arrleft = no_left*[nxt]

    no_right = b - c

    if no_right < 0:
        return 'IMPOSSIBLE'
    else:
        arrright = no_right * [nxt]

    totleft = n - (len(arr) + len(arrleft) + len(arrright))
    print(arr, arrleft, arrright)
    if totleft<0:
        return 'IMPOSSIBLE'
    elif totleft > 0:
        if len(arr) < 2:
            if nxt - 1 <= 0:
                return 'IMPOSSIBLE'
            if len(arrleft)>0:
                arr = arrleft + [nxt - 1] * totleft + arr + arrright
            elif len(arrright)>0:
                arr = arrleft + arr + [nxt - 1] * totleft  + arrright
            else:
                return 'IMPOSSIBLE'

        else:
            arr.pop()
            arr = arrleft + arr +  [nxt] *totleft + [n] + arrright
    else:
        arr = arrleft + arr + arrright

    return ' '.join([str(i) for i in arr])



print(high_buildings(5 ,3, 3, 2))


def high_buildings(n, a, b, c):
    no_middle = c
    arr = [n] * c
    no_left = a - c
    if arr:
        nxt = n - 1
    else:
        nxt = n
    if no_left < 0:
        return 'IMPOSSIBLE'
    else:
        arrleft = no_left * [nxt]

    no_right = b - c

    if no_right < 0:
        return 'IMPOSSIBLE'
    else:
        arrright = no_right * [nxt]

    totleft = n - (len(arr) + len(arrleft) + len(arrright))
    print(arr, arrleft, arrright)
    if totleft < 0:
        return 'IMPOSSIBLE'
    elif totleft > 0:
        if len(arr) < 2:
            if nxt - 1 <= 0:
                return 'IMPOSSIBLE'
            if len(arrleft) > 0:
                arr = arrleft + [nxt - 1] * totleft + arr + arrright
            elif len(arrright) > 0:
                arr = arrleft + arr + [nxt - 1] * totleft + arrright
            else:
                return 'IMPOSSIBLE'

        else:
            arr.pop()
            arr = arrleft + arr + [nxt] * totleft + [n] + arrright
    else:
        arr = arrleft + arr + arrright

    return ' '.join([str(i) for i in arr])





def subsets(s):
    sets = []
    for i in range(1, 1 << len(s)):
        subset = [s[bit] for bit in range(len(s)) if is_bit_set(i, bit)]
        sets.append(subset)
    return sets[::-1]

def is_bit_set(num, bit):
    return num & (1 << bit) > 0

def toys(n,e_all, r_all):
    sets =subsets(list(range(n)))
    max_sm = 0
    no_toys = n
    for st in sets:
        e_all_s = [e_all[i] for i in st]
        r_all_s = [r_all[i] for i in st]
        sm = sum(e_all_s)
        fnd = 0
        fin_sm = 0
        for k in range(len(e_all_s)):
            if e_all_s[k] + r_all_s[k] > sm:
                fin_sm = sm + sum(e_all_s[:k])
                fnd = 1

        if fnd == 0:
            return 'INDEFINITE', str(n - len(st))
        else:
            if max_sm > fin_sm:
                max_sm = fin_sm
                no_toys = n - len(st)






    return str(max_sm), str(no_toys)


n= 4

e_all = [1,2,3,1]
r_all = [1,1,1,1]



o  = toys(n, e_all, r_all )


print(subsets([1,2,3,4]))


