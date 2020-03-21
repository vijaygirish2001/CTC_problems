'''

Magic Index: A magic index in an array A[ 1 .•. n-1] is defined to be an index such that A[ i]
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
FOLLOW UP
What if the values are not distinct?
'''

def magic_ind(A, l,r):
    mid = int((l+r)/2)
    if l>r:
        return None
    if A[mid] == mid:
        return mid
    elif A[mid] > mid:
        magic_ind(A, l, mid-1)
    else:
        magic_ind(A, mid+1,r)


def magic_ind_non(A, l,r):
    mid = int((l+r)/2)
    if l>r:
        return None
    if A[mid] == mid:
        return mid

    magic_ind(A, l, min(A[mid],mid-1))

    magic_ind(A, max(mid+1,A[mid]),r)

A = [-1,0,2,3,5,8]


print(magic_ind_non(A, 0,len(A)-1))








