'''
2. Find the next permutation of a number

next_permutation(12) = 21
next_permutation(315) = 351
next_permutation(583) = 835
next_permutation(12389) = 12398
next_permutation(34722641) = 34726421

'''


def next_permutation(n):

    n = list(str(n))
    ind = len(n) - 2
    while ind >= 0:

        if n[ind+1] > n[ind]:

            arr = sorted(n[ind+1:])

            for j in range(0,len(arr)):
                if arr[j]> n[ind]:
                    temp =  n[ind]
                    #print(n[ind] , arr[j])
                    n[ind] = arr[j]
                    arr[j] = temp
                    break


            break
        ind-=1


    return int(''.join(n[:ind+1] + arr))

n = 34722641
print(next_permutation(n))