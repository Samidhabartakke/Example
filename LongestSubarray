def longestSubarray(arr, n, k):
    Max = 1
    s = set()

    for i in range(n - 1):
        s.add(arr[i])
        for j in range(i + 1, n):
            if (abs(arr[i] - arr[j]) == 0 or abs(arr[i] - arr[j]) == k):
                if (not arr[j] in s):
                    if (len(s) == 2):
                        break
                    else:
                        s.add(arr[j])
            else:
                break
        if (len(s) == 2):
            Max = max(Max, j - i)
            s.clear()
        else:
            s.clear()
    return Max

if __name__ == '__main__':
    arr = [1, 6, 6, 1, 7, 3,4, 6, 5]
    N = 9
    K = 5
    length = longestSubarray(arr, N, K)
    print(length)
