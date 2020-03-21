'''
In stock market , a person buys a stock and sells it on some future date. Given the stock prices of N days in an form of an array A[ ] and a positive integer K, find out the maximum profit a person can make in atmost K transactions. A transaction is equivalent to (buying + selling) of a stock and new transaction can start only when the previous transaction has been completed.In stock market , a person buys a stock and sells it on some future date. Given the stock prices of N days in an form of an array A[ ] and a positive integer K, find out the maximum profit a person can make in atmost K transactions. A transaction is equivalent to (buying + selling) of a stock and new transaction can start only when the previous transaction has been completed.
'''
import numpy as np

A ='1 5 9 2 6'

A = [1,5,9,2,6]
N=5
K=2

d = np.zeros((N + 1, K + 1))
for i in range(2, N + 1):
    for j in range(1, K + 1):
        d[i][j] = max(d[i - 1, j], max([d[t][j - 1] + max(A[i-1] - A[t-1], 0) for t in range(1, i)]))


print(d[5,2])
