# Given a rope of length n meters, cut the rope in different parts of integer lengths
# in a way that maximizes product of lengths of all parts
# Eg: n = 10 ==> 3 + 3 + 4 = 10 ==> 3 * 3 * 4 = 36


def MaximumProductRodCutting(n):
    dp = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i // 2 + 1):  # range(i) would also result the same
            # max(i - j, dp[i - j])
            # => eg: max(3, dp[3]) => dp[3] = 1 * 2 = 2
            dp[i] = max(dp[i], j * max(i - j, dp[i - j]))

    return dp[n]


n = 15
print(MaximumProductRodCutting(n))
