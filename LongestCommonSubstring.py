def LongestCommonsubstring(X, m, Y, n):
    maxLength = 0
    endingIndex = 0

    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > maxLength:
                    maxLength = dp[i][j]
                    endingIndex = i
    # here dp[m][n] may be zero since they may not end with same letter
    return X[endingIndex - maxLength:endingIndex]


X = 'Preethi'
Y = 'reeth'
print(LongestCommonsubstring(X, len(X), Y, len(Y)))
