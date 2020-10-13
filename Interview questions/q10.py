
'''

Please Pass the Coded Messages
==============================

You need to pass a message to the bunny prisoners, but to avoid detection, the code you agreed to use is... obscure, to say the least. The bunnies are given food on standard-issue prison plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.

You have L, a list containing some digits (0 to 9). Write a function solution(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the solution. L will contain anywhere from 1 to 9 digits.  The same digit may appear multiple times in the list, but each element in the list may only be used once.
'''
def solution(x):

    def is_part(x1,x2):
        for i in x1:
            if i in x2:
                x2.remove(i)
            else:
                return False
        return True
    #print(x)
    x = sorted(x)
    val = 0
    ind = 0
    for i in x:
        val += 10**ind * i
        ind += 1
    #print(val)
    if val % 3 == 0:
        return val
    h_fact = val // 3 + 1


    while h_fact > 0:
        x_str = [str(i) for i in x]
        s_pres = str(int(h_fact * 3))
        s_pres_l = list(s_pres)
        if is_part(s_pres_l,x_str):
            return int(s_pres)
        h_fact -= 1
        print(h_fact)

    return 0


def solution(x):
    def chk_res(x, arg):
        ind = 0
        if arg == 1:
            arg1 = 2
        else:
            arg1 = 1
        rem = [-1] * 2
        while ind < len(x):

            if x[ind] % 3 == arg:
                x.remove(x[ind])
                return ''.join([str(i) for i in x[::-1]])

            if x[ind] % 3 == arg1:
                if rem[0] == -1:
                    rem[0] = x[ind]

                elif rem[1] == -1:
                    rem[1] = x[ind]
            ind += 1
        if rem[0] != -1 and rem[1] != -1:
            x.remove(rem[0])
            x.remove(rem[1])
            return ''.join([str(i) for i in x[::-1]])
        return False

    x = sorted(x)
    x_sum = sum(x)
    # print(x_sum)
    if x_sum == 0:
        return 0
    if x_sum % 3 == 0:
        return int(''.join([str(i) for i in x[::-1]]))
    elif x_sum % 3 == 1:
        res = chk_res(x, 1)
        if res:
            return int(res)
    elif x_sum % 3 == 2:
        res = chk_res(x, 2)
        if res:
            return int(res)

    return 0


y = solution([9,8,6,8,6])

print((y))
