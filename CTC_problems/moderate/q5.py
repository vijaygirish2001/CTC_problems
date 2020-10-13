'''
16.5 Factorial zeros: Write an algorithm which computes the number of trailing zeros in n factorial
'''

def fact_zeros(n):
    noz= 0
    for i in range(5,n+1):
        k = i
        while k%5 == 0 and k>0:
            noz+=1

            k=k/5
    return noz


print(fact_zeros(15))
