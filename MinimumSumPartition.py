import sys


# Given a set of integers, the task is to divide it into two sets S1 and S2
# such that the absolute difference between their sums is minimum.
# Example:  arr[] = {1, 6, 11, 5} => Output (difference): 1
# => Subset1 = {1, 5, 6}, Subset2 = {11}


def MinimumSumPartition(arr):
    totalSum = sum(arr)
    n = len(arr)
    dp = SubsetSum(arr, n, totalSum)  # totalSum / 2 => is sufficient!
    diff = sys.maxsize
    for subsetSum in range(totalSum // 2, -1, -1):
        if dp[n][subsetSum]:
            print('Sum of one set is', subsetSum)
            print('Sum of other set is', totalSum - subsetSum)
            diff = (totalSum - subsetSum) - subsetSum
            break
    print('The Minimum Difference between 2 sets is ', diff)


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

    return dp


arr = [3, 1, 4, 2, 2, 1]
MinimumSumPartition(arr)
