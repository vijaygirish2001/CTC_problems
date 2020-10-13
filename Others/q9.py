'''
Colorful Numbers
Objective: Given a number, find out whether its colorful or not.

Colorful Number: When in a given number, product of every digit of a sub-sequence are different. That number is called Colorful Number. See Example

Example:
'''


def is_colorful(n):

    arr_digits = list(str(n))
    arr_digits = [int(i) for i in arr_digits]

    prod_list = []

    def all_subsequence(arr,ind, subseq, prod ):

        if ind >= len(arr):
            if subseq:
                print(subseq, prod)
                if prod in prod_list:
                    return False
                prod_list.append(prod)
            return True

        chk  = all_subsequence(arr, ind+1, subseq + [arr[ind]], prod* arr[ind])
        if not chk:
            return False

        chk = all_subsequence(arr, ind + 1, subseq, prod)
        if not chk:
            return False

        return True

    return all_subsequence(arr_digits, 0, [], 1)


print(is_colorful('326'))


def  sm(a,b):
    a+=1
    print(a,b)
    return a+b

def cc(a,b):
    sm(a,b)
    print(a,b)


cc(1,2)

