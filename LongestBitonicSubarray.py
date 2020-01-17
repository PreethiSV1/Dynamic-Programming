def LongestBitonicSubarrayLength(X, m):
    LIS = [0 for _ in range(m)]
    LDS = [0 for _ in range(m)]

    # from first number
    LIS[0] = 1
    for i in range(1, m):
        LIS[i] = 1
        if X[i - 1] < X[i]:
            LIS[i] = LIS[i - 1] + 1

    # from last number
    LDS[m - 1] = 1
    for i in reversed(range(m - 1)):
        LDS[i] = 1
        if X[i] > X[i + 1]:
            LDS[i] = LDS[i + 1] + 1

    longestBSLength = 1
    beg, end = 0, 0
    for i in range(0, m):
        if longestBSLength < LDS[i] + LIS[i] - 1:
            longestBSLength = LDS[i] + LIS[i] - 1
            beg = i - LIS[i] + 1
            end = i + LDS[i] - 1

    return longestBSLength, X[beg : end + 1]


X = [3, 5, 8, 4, 5, 9, 10, 8, 5, 3, 4]
m = len(X)
print(LongestBitonicSubarrayLength(X, m))
