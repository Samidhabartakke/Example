import math
def countRect(n):
    ans = 0
    for length in range(1, int(math.sqrt(n)) + 1):
        height = length
        while (height * length <= n):
            # height >= length is maintained
            ans += 1
            height += 1
    return ans


# Driver code
n = 2
n1 = 6
print(countRect(n))
print(countRect(n1))
