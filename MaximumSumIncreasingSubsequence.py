# Function to find maximum sum of increasing subsequence in an array
# eg: [8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11] => 34 ==> [8, 12, 14]
def MaximumSumIncreasingSubsequence(X, m):
    sumDp = [0 for _ in range(m)]

    # to store (maximum sum increasing) subsequence till each i-th index
    MSIS = [[] for _ in range(m)]

    # sum will be the number itself at index 0
    sumDp[0] = X[0]
    MSIS[0].append(X[0])

    for i in range(1, m):
        for j in range(i):
            if X[i] > X[j] and sumDp[i] < sumDp[j]:
                MSIS[i] = MSIS[j].copy()
                sumDp[i] = sumDp[j]
        # include i-th element in the sum
        sumDp[i] += X[i]
        MSIS[i].append(X[i])

    maxSum = 0
    for i in range(1, m):
        if sumDp[i] > sumDp[maxSum]:
            maxSum = i

    return sumDp[maxSum], MSIS[maxSum]


X = [8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11]
m = len(X)
maxSum, maxSequence = MaximumSumIncreasingSubsequence(X, m)
print(maxSum)
print(maxSequence)
