# Find LIS in 2 methods
def LongestIncreasingSubsequence(X, m):
    # method 1
    print(LongestIncreasingSubsequenceNew(X, m))

    Y = sorted(X)
    # method 2 =>>> LCS(X, m, sorted(X), m)
    dp = LongestCommonSubsequenceLengthInt(X, m, Y, m)
    print(LongestCommonSubsequenceInt(X, m, Y, m, dp))


# Function to find LCS Length of Integer numbers
def LongestCommonSubsequenceLengthInt(X, m, Y, n):
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp


# Function to find LCS of Integer numbers
# that outputs the sequence as a string
def LongestCommonSubsequenceInt(X, m, Y, n, dp):
    if m == 0 or n == 0:
        return ''

    if X[m - 1] == Y[n - 1]:
        return LongestCommonSubsequenceInt(X, m - 1, Y, n - 1, dp) + str(X[m - 1]) + " "

    if dp[m - 1][n] > dp[m][n - 1]:
        return LongestCommonSubsequenceInt(X, m - 1, Y, n, dp)

    return LongestCommonSubsequenceInt(X, m, Y, n - 1, dp)


# Function to find LIS without using LCS
def LongestIncreasingSubsequenceNew(X, m):
    dp = [[] for _ in range(m)]

    # starting with index 0 => LIS length = 1
    dp[0].append(X[0])
    for i in range(1, m):
        for j in range(i):
            if X[i] > X[j] and len(dp[i]) < len(dp[j]) + 1:
                # include previous number's sequence
                # if the current number is greater than previous number
                dp[i] = dp[j].copy()
        # include i-th value in the sequence
        dp[i].append(X[i])

    maximum = dp[0]
    for i in dp:
        if len(maximum) < len(i):
            maximum = i

    return maximum


X = [3, 2, 6, 4, 5, 1]
LongestIncreasingSubsequence(X, len(X))
