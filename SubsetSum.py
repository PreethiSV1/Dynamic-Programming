# Modification of Knapsack Problem <==== Important
# Function to check if a subset with given sum is possible
def SubsetSum(arr, n, sum):
    dp = [[False for _ in range(sum + 1)] for _ in range(n + 1)]

    # if 0 items in the list and sum is non-zero
    for i in range(sum + 1):
        dp[0][i] = False

    # if sum is zero
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] > j:  # don't include ith element if j - arr[i-1] is negative
                dp[i][j] = dp[i - 1][j]
            else:
                # can a subset be formed
                # either including OR excluding the current number
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]

    return dp[n][sum]


arr = [7, 3, 2, 5, 8]
n = len(arr)
requiredSum = 18
print(SubsetSum(arr, n, requiredSum))