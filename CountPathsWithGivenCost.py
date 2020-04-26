# Function to return the count of paths with given cost
# to reach cell at (i,j) in the matrix X from first cell


def CountPathsWithGivenCost(X, i, j, cost, dp):
    if cost < 0:
        return 0

    # if we are at first cell, check if => 1st cell's cost - available cost = 0
    if i == 0 and j == 0:
        if X[0][0] - cost == 0:
            return 1
        else:
            return 0

    key = str(i) + '|' + str(j) + '|' + str(cost)
    if dp.get(key) is None:
        # each step, we subtract that cell's cost
        if i == 0:
            dp[key] = CountPathsWithGivenCost(X, i, j - 1, cost - X[i][j], dp)

        elif j == 0:
            dp[key] = CountPathsWithGivenCost(X, i - 1, j, cost - X[i][j], dp)

        else:
            dp[key] = CountPathsWithGivenCost(X, i - 1, j, cost - X[i][j], dp) \
                       + CountPathsWithGivenCost(X, i, j - 1, cost - X[i][j], dp)
    return dp[key]


X = [
    [4, 7, 1, 6],
    [5, 7, 3, 9],
    [3, 2, 1, 2],
    [7, 1, 6, 3]
]
m = len(X)
n = len(X[0])
dp = {}
print(CountPathsWithGivenCost(X, m - 1, n - 1, 24, dp))
