# Modification of Subset sum problem
# Partition problem - Return true if given array arr[0..n-1] can
# be divided into two subsets with equal sum
def PartitionSum(arr):
    total = sum(arr)
    return (not (total % 2)) and SubsetSum(arr, len(arr), total // 2)


# Function to check if a subset with given sum is possible
def SubsetSum(arr, n, sum):
    dp = [[False for _ in range(sum + 1)] for _ in range(n + 1)]

    # if number of items(n)is zero and sum is non zero
    for i in range(sum + 1):
        dp[0][i] = False

    # if sum is zero and n is non zero
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # either including (decrement the sum) OR
                # excluding the element can give the required subset
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]

    return dp[n][sum]


arr = [7, 3, 1, 5, 4, 8]
n = len(arr)
print(PartitionSum(arr))
