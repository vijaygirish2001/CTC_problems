'''
Last updated: Mar 22 2020, 09:30

Problem
There are N houses for sale. The i-th house costs Ai dollars to buy. You have a budget of B dollars to spend.

What is the maximum number of houses you can buy?

Input
The first line of the input gives the number of test cases, T. T test cases follow.
Each test case begins with a single line containing the two integers N and B. The second line contains N integers.
 The i-th integer is Ai, the cost of the i-th house.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum number of houses you can buy.

Limits
Time limit: 15 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ B ≤ 105.
1 ≤ Ai ≤ 1000, for all i.

Test set 1
1 ≤ N ≤ 100.

Test set 2
1 ≤ N ≤ 105.
'''


def max_houses(cst, N, B):
    no_house = [0] * N
    sm = 0
    cst = sorted(cst)
    k = 0
    while k < N:
        if k == 0:
            if cst[k] <= B:
                no_house[k] = 1
                sm = cst[k]
        else:
            if sm + cst[k] <= B:
                no_house[k] = no_house[k - 1] + 1
                sm += cst[k]
            else:
                no_house[k] = no_house[k - 1]

        k += 1

    return no_house[N - 1]


t = int(input())
for i in range(t):
    inp = input().split()
    inp = [int(j) for j in inp]
    N = inp[0]
    B = inp[1]

    cst = input().split()
    cst = [int(j) for j in cst]

    nohs = max_houses(cst, N, B)
    print('Case #' + str(i + 1) + ': ' + str(nohs))



