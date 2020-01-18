# Function to find longest bitonic subarray (continuous numbers --> subarray)
# bitonic ---> Increases and then decreases eg: 1 4 7 10 6 3 (1 < 4 < 7 < 10 > 6 > 3)
def LongestBitonicSubarray(X, m):
    LIS = [0 for _ in range(m)]
    LDS = [0 for _ in range(m)]

    # from first number
    LIS[0] = 1
    for i in range(1, m):
        LIS[i] = 1
        if X[i - 1] < X[i]:
            # only if prev number is smaller than current
            LIS[i] = LIS[i - 1] + 1

    # from last number
    LDS[m - 1] = 1
    for i in reversed(range(m - 1)):
        LDS[i] = 1
        if X[i] > X[i + 1]:
            # only if next number is smaller than current
            LDS[i] = LDS[i + 1] + 1

    longestBSLength = 1
    beg, end = 0, 0
    for i in range(0, m):
        if longestBSLength < LDS[i] + LIS[i] - 1:
            longestBSLength = LDS[i] + LIS[i] - 1
            beg = i - LIS[i] + 1  # current index - length of LIS at i
            end = i + LDS[i] - 1  # current index + length of LDS at i

    return longestBSLength, X[beg: end + 1]


X = [3, 5, 8, 4, 5, 9, 10, 8, 5, 3, 4]
m = len(X)
length, subarray = LongestBitonicSubarray(X, m)
print(length)
print(subarray)
