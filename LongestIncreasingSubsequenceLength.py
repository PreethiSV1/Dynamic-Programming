# Function to simply find the length of LIS without using LCS
def LongestIncreasingSubsequenceLength(X, m):
    dp = [0 for i in range(m)]

    # starting with index 0 => LIS length = 1
    dp[0] = 1

    for i in range(1, m):
        dp[i] = 1
        for j in range(i):
            if X[i] > X[j] and dp[i] < dp[j]:
                # If current number is greater than the previous,
                # copy the previous number's LIS value
                dp[i] = dp[j]
        # include i-th value in the sequence length
        dp[i] += 1
    return max(dp)


X = [10, 22, 9, 33, 21, 50, 41, 60]
print(LongestIncreasingSubsequenceLength(X, len(X)))
