def maxLen(n, arr):
    #Code here
    sumArr = [arr[0]]
    pair = {}
    max_len = 0
    for i in range(1, len(arr)):
        sumArr.append(arr[i]+sumArr[i-1])
    
    for i in range(len(arr)):
        if sumArr[i] in pair.keys():
            max_len = max(max_len, abs(i - pair[sumArr[i]]))
        else:
            pair[sumArr[i]] = i
        if sumArr[i] == 0:
            max_len = max(max_len, i+1)
    return max_len