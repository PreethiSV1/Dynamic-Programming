# Function to find the length of shortest string (supersequence)
# that contains both X and Y as subsequences
# Eg: 'diet', 'meet' => 'dimeet' ==> 6
def ShortestCommonSupersequenceLength(X, m, Y, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # if any of X or Y is empty, scs contains length
    # which is equal to the other string's length
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if both are same letters, then it only adds 1 to the SCS length
            # di, me => dime but die (4) , mee => dimee (5 instead of 6)
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            # Else, the minimum of SCS of 2 sequences + 1
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)
    return dp[m][n]


X = "ABCBDAB"
Y = "BDCABA"
print(ShortestCommonSupersequenceLength(X, len(X), Y, len(Y)))
