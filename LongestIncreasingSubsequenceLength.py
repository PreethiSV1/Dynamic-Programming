def LongestIncreasingSubsequenceLength(X, m):
    dp = [0 for i in range(m)]

    # starting with index 0 => LIS length = 1
    dp[0] = 1

    for i in range(1, m):
        dp[i] = 1
        for j in range(i):
            if X[i] > X[j] and dp[i] < dp[j]:
                dp[i] = dp[j]
        # include i in the sequence
        dp[i] += 1
    return max(dp)


X = [10, 22, 9, 33, 21, 50, 41, 60]
print(LongestIncreasingSubsequenceLength(X, len(X)))