# Note - LCSubstring of X and sorted(X) cannot work
# => Eg: X = 3 1 2 4 5
# sorted(X) = 1 2 3 4 5
# LCSubstring would give [1, 2] whereas answer = [1, 2, 4]


def LongestIncreasingSubarray(arr, n):
    # 'maxLength' to store the length of longest increasing subarray
    # 'length' to store the lengths of longest increasing subarray at different instants of time
    maxLength = 1
    length = 1
    endingIndex = 0

    # traverse the array from the 2nd element 
    for i in range(1, n):

        # if current element if greater than previous 
        # add up to the previous increasing subarray encountered so far
        if arr[i] > arr[i - 1]:
            length = length + 1
        else:
            if maxLength < length:
                maxLength = length
                endingIndex = i

            # reset 'length' to 1 as from this element 
            # again the length of the new increasing 
            # subarray is being calculated     
            length = 1

            # comparing the length of the last 
    # increasing subarray with 'maxLength' 
    if maxLength < length:
        maxLength = length
        endingIndex = n

    return arr[endingIndex - maxLength: endingIndex]


X = [5, 6, 3, 5, 7, 8, 9, 1, 2]
print(LongestIncreasingSubarray(X, len(X)))
