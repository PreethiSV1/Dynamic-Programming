def LongestBitonicSubsequenceLength(X, m):
    LIS = [0 for _ in range(m)]
    LDS = [0 for _ in range(m)]

    # from first number
    LIS[0] = 1
    for i in range(1, m):
        for j in range(i):
            if X[i] > X[j] and LIS[i] < LIS[j]:
                LIS[i] = LIS[j]
        LIS[i] += 1

    # from last number
    LDS[m - 1] = 1
    for i in reversed(range(m - 1)):
        for j in reversed(range(i - 1, m)):
            if X[i] > X[j] and LDS[i] < LDS[j]:
                LDS[i] = LDS[j]
        LDS[i] += 1

    longestBSLength = LIS[0] + LDS[0] - 1
    for i in range(1, m):
        longestBSLength = max(longestBSLength, LIS[i] + LDS[i] - 1)

    return longestBSLength


def LongestBitonicSubsequence(X, m):
    LIS = [[] for _ in range(m)]
    LDS = [[] for _ in range(m)]

    # from first number
    LIS[0].append(X[0])
    for i in range(1, m):
        for j in range(i):
            if X[i] > X[j] and len(LIS[i]) < len(LIS[j]):
                LIS[i] = LIS[j].copy()
        LIS[i].append(X[i])

    # from last number
    LDS[m - 1].append(X[m - 1])
    for i in reversed(range(m - 1)):
        for j in reversed(range(i - 1, m)):
            if X[i] > X[j] and len(LDS[i]) < len(LDS[j]):
                LDS[i] = LDS[j].copy()
        LDS[i].insert(0, X[i])

    peak = 0
    for i in range(1, m):
        if (len(LIS[i]) + len(LDS[i])) > (len(LIS[peak]) + len(LDS[peak])):
            peak = i    # Maximum increasing followed by decreasing sequence's position

    return LIS[peak][:-1] + LDS[peak]    # since peak index's value will be present in both


X = [4, 2, 5, 9, 7, 6, 10, 3, 1]
m = len(X)
print(LongestBitonicSubsequenceLength(X, m))
print(LongestBitonicSubsequence(X, m))
