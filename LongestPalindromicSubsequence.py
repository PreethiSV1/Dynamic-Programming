# Find length directly
def LongestPalindromicSubsequenceLength(X):
    n = len(X)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if X[i] == X[j] and j == i + 1:
                dp[i][j] = 2
            elif X[i] == X[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    return dp[0][n - 1]


# Function to find Longest Palindromic sequence using LCS with
# String X and String Y = reverse of X
def LongestPalindromicSubsequence(X):
    Y = X[::-1]
    m = len(X)
    dp = LongestCommonSubsequenceLength(X, m, Y, m)
    return LongestCommonSubsequence(X, m, Y, m, dp)


# Function to find Longest Common Subsequence Length
# eg: ABCDEF, BGDAE ==> 3
def LongestCommonSubsequenceLength(X, m, Y, n):
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp


# Function to find Longest Common Subsequence
# eg: ABCDEF, BGDAE ==> BDE
def LongestCommonSubsequence(X, m, Y, n, dp):
    if m == 0 or n == 0:
        return ''

    if X[m - 1] == Y[n - 1]:
        return LongestCommonSubsequence(X, m - 1, Y, n - 1, dp) + X[m - 1]

    if dp[m - 1][n] > dp[m][n - 1]:
        return LongestCommonSubsequence(X, m - 1, Y, n, dp)

    return LongestCommonSubsequence(X, m, Y, n - 1, dp)


X = "abacdfgdcaba"
print(LongestPalindromicSubsequenceLength(X))
print(LongestPalindromicSubsequence(X))
