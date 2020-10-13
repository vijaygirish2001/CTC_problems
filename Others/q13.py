'''
Edit distance
'''

def edit_distance(wrd1, wrd2):
    n1 = len(wrd1)
    n2 = len(wrd2)

    dp = [[0 for i in range(n2+1)] for j in range(n1+1)]


    for i in range(1, n1+1):
        dp[i][0] = i

    for i in range(1, n2+1):
        dp[0][i] = i

    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if wrd1[i-1] == wrd2[j-1]:
                c = 0
            else:
                c = 1
            dp[i][j] = min(dp[i-1][j-1]+c,dp[i-1][j]+1, dp[i][j-1]+1 )

    return dp[n1][n2]


print(edit_distance('hello', 'hell'))






