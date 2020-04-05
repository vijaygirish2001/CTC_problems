'''
Problem
Dr. Patel has N stacks of plates. Each stack contains K plates. Each plate has a positive beauty value, describing how beautiful it looks.

Dr. Patel would like to take exactly P plates to use for dinner tonight. If he would like to take a plate in a stack, he must also take all of the plates above it in that stack as well.

Help Dr. Patel pick the P plates that would maximize the total sum of beauty values.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the three integers N, K and P. Then, N lines follow. The i-th line contains K integers, describing the beauty values of each stack of plates from top to bottom.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum total sum of beauty values that Dr. Patel could pick.
'''
import numpy as np

def recur_plate(beau_val):
    dp = np.zeros((n+1,p+1))

    for i in range(n):
        for j in range(p+1):
            for m in range( min(k, p - j)+1):
                if m >0:
                    print(i,j,m,dp[i + 1][j + m], dp[i][j])
                    dp[i + 1][j + m] = max(dp[i + 1][j + m], dp[i][j] + beau_val[i][m-1])
                else:
                    dp[i + 1][j + m] = dp[i + 1][j + m]

    return dp[n][p]


t = int(input())
for i in range(t):
    inp = input().split()
    inp = [int(j) for j in inp]
    n, k, p = inp

    beau_val = [[0] * k] * n
    for m in range(n):
        inp = input().split()
        inp = [int(j) for j in inp]
        beau_val[m] = inp



    c = [[-1] * n * k] * n
    part_sum = recur_plate(beau_val)

    print('Case #' + str(i + 1) + ': ' + str(part_sum))



