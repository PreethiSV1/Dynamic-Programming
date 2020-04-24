# Initially find LCS of the strings X and Y, then find if
# the other characters in the string are deleted from X or inserted into Y
def LongestCommonSubsequenceLength(X, m, Y, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    print(dp[m][n])
    return dp


# To output the differences with '+' or '-' symbol for the differences between X and Y
def DiffUtility(X, m, Y, n):
    # Character present both in X and Y
    if m > 0 and n > 0 and X[m - 1] == Y[n - 1]:
        DiffUtility(X, m - 1, Y, n - 1)
        print(' ' + X[m - 1], end='')

    # Character present in X and not in Y
    elif m > 0 and (n == 0 or dp[m - 1][n] > dp[m][n - 1]):
        DiffUtility(X, m - 1, Y, n)
        print(' -' + X[m - 1], end='')

    # Character present in Y and not in X
    elif n > 0 and (m == 0 or dp[m][n - 1] >= dp[m - 1][n]):
        DiffUtility(X, m, Y, n - 1)
        print(' +' + Y[n - 1], end='')


X = 'Hellloworld'
Y = 'HelloWorld!'
m, n = len(X), len(Y)
dp = LongestCommonSubsequenceLength(X, m, Y, n)
DiffUtility(X, m, Y, n)
