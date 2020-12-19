def replaceDig(x, from1, to):
    result = 0
    multiply = 1

    while (x > 0):
        reminder = x % 10
        if (reminder == from1):
            result = result + to * multiply

        else:
            result = result + reminder * multiply

        multiply *= 10
        x = int(x / 10)
    return result

def calculateMinMaxSum(x1, x2):
    minSum = replaceDig(x1, 6, 5) + replaceDig(x2, 6, 5)
    maxSum = replaceDig(x1, 5, 6) + replaceDig(x2, 5, 6)
    print("Minimum sum =", minSum)
    print("Maximum sum =", maxSum, end=" ")
# Driver code
if __name__ == '__main__':
    x1 = 45
    x2 = 64
    calculateMinMaxSum(x1, x2)
    x3 = 11
    x4 = 53
    calculateMinMaxSum(x3, x4)
