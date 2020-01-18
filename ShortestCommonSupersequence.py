# Function to find the length of shortest string (supersequence)
# that contains both X and Y as subsequences and store in dp
def ShortestCommonSupersequenceLength(X, m, Y, n):
    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1) # shortest => minimum
    return dp


# Function to print the shortest string (supersequence)
# that contains both X and Y as subsequences
# Eg: 'diet', 'meet' => 'dimeet'
def ShortestCommonSupersequence(X, m, Y, n):

    if m == 0: # if we have reached the end of first string
        return Y[:n]

    if n == 0: # if we have reached the end of second string
        return X[:m]

    if X[m - 1] == Y[n - 1]: # if both characters are same
        return ShortestCommonSupersequence(X, m - 1, Y, n - 1) + X[m - 1]

    if dp[m][n - 1] < dp[m - 1][n]:
        return ShortestCommonSupersequence(X, m, Y, n - 1) + Y[n - 1]

    return ShortestCommonSupersequence(X, m - 1, Y, n) + X[m - 1]


X = "meet"
Y = "diet"
m, n = len(X), len(Y)
dp = ShortestCommonSupersequenceLength(X, m, Y, n)
print(ShortestCommonSupersequence(X, m, Y, n))