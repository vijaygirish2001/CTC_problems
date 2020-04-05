'''
8.11 Coins: Given an infinite number of quarters (25 cents), dimes (1 O cents), nickels (5 cents), and
pennies (1 cent), write code to calculate the number of ways of representing n cents.
'''
ways = []
tot = 20
dc = {}


def noways(n, lst, memo, ind,dc):
    if ind > len(lst)-1:
        if n ==0:
            ways.append(str(dc))
            return 1
        else:

            return 0



    if (ind, n) in memo:
        return memo[(ind,n)]

    nw = 0
    denom = lst[ind]
    k=0
    if n==tot:
        dc={}
    while n-k*denom>=0:
        #print(nw,n- k*denom, lst, memo, ind,k)
        if n- k*denom<tot:
            dc[denom]= k
        nw += noways(n- k*denom, lst, memo, ind+1,dc)
        k+=1
    memo[(ind,n)] = nw
   # print(memo)
    return nw


n=20
memo = {}
b= noways(n, [25,10,5], memo,0,dc)
print(b)