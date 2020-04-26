# Function to calculate minimum cost to reach a cell at position (m,n) in any matrix
def MinimumCostPath(Cost, m, n):
    dp = [[0 for _ in range(n)] for _ in range(m)]

    dp[0][0] = Cost[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + Cost[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + Cost[0][j]
    for i in range(1, m):
        for j in range(1, n):
            # only right (dp[i - 1][j]) and down (dp[i][j - 1]) moves are possible
            # to include moving diagonally, include dp[i - 1][j - 1]
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + Cost[i][j]
    return dp[m - 1][n - 1]


cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(MinimumCostPath(cost, len(cost), len(cost[0])))
