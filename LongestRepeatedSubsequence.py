# Function to find longest non-overlapping repeating subsequence's length
# concept - to find LCS of X (i) with X (j) itself, also check if => i != j
# eg: ATACTCGGA => 4
def LongestRepeatingSubsequenceLength(X, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    # Start from index 1 (to check X[i - 1] == X[j - 1])
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if X[i - 1] == X[j - 1] and i != j:  # i != j => non-overlapping
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # Maximum length
    print(dp[n][n])
    return dp


# Function to find longest non-overlapping repeating subsequence's length
# eg: ATACTCGGA => ATCG
def LongestRepeatingSubsequence(X, m, n, dp):
    if m == 0 or n == 0:
        return ''

    if X[m - 1] == X[n - 1] and m != n:
        return LongestRepeatingSubsequence(X, m - 1, n - 1, dp) + X[m - 1]

    if dp[m - 1][n] > dp[m][n - 1]:
        return LongestRepeatingSubsequence(X, m - 1, n, dp)

    return LongestRepeatingSubsequence(X, m, n - 1, dp)


X = "ATACTCGGA"  # ATCG
n = len(X)
dp = LongestRepeatingSubsequenceLength(X, n)
print(LongestRepeatingSubsequence(X, n, n, dp))
