# Given a value N, if we want to make change for N cents,
# and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins,
# to find out the number of ways can we make the change.
# amount = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}


def CoinChangeCountWays(arr, target):
    n = len(arr)
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1

    for i in range(n):
        for j in range(target + 1):
            if arr[i] <= j:
                dp[j] += dp[j - arr[i]]
    return dp[target]


coins = [1, 2, 3]
amount = 4
print(CoinChangeCountWays(coins, amount))
