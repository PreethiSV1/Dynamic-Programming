import sys


# Given coins of different denominations and a total amount of money 'amount'
# function to compute the fewest number of coins that you need to make up that amount
# coins = [1, 2, 5], amount = 11 => min coins = 3 (Explanation: 11 = 5 + 5 + 1)


def CoinChangeMinimumCoins(coins, amount):
    dp = [sys.maxsize for _ in range(amount + 1)]
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != sys.maxsize:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return -1 if dp[amount] == sys.maxsize else dp[amount]


arr = [1, 3, 5, 7]
print(CoinChangeMinimumCoins(arr, 10))
