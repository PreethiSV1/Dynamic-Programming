def LongestCommonSubsequenceLength(X, m, Y, n):
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp

def LongestCommonSubsequence(X, m, Y, n, dp):
    if m == 0 or n == 0:
        return ''

    if X[m-1] == Y[n-1]:
        return LongestCommonSubsequence(X, m-1, Y, n-1, dp) + X[m-1]

    if dp[m-1][n] > dp[m][n-1]:
        return LongestCommonSubsequence(X, m-1, Y, n, dp)

    return LongestCommonSubsequence(X, m, Y, n-1, dp)

X = 'ABBABBA'
Y = 'BABABA'
m = len(X)
n = len(Y)
dp = LongestCommonSubsequenceLength(X, m, Y, n)
print(LongestCommonSubsequence(X, m, Y, n, dp))