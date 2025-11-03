def vecSum(v1, v2):
    sum0 = [0] * len(v1)
    if len(v1) != len(v2):
        return -1 # error state
    else:
        for i in range(len(v1)):
            sum0[i] = v1[i] + v2[i]
    return sum0

def dotProduct(v1, v2):
    sum0 = 0
    if len(v1) != len(v2):
        return -1 # error state
    else:
        for i in range(len(v1)):
            sum0 += v1[i] * v2[i]
    return sum0

def shiftIt(v):
    v2 = []
    if isinstance(v, list):
        v2 = [0] * len(v)
        for i in range(len(v)):
            j = (i + 2) % len(v)
            v2[j] = v[i]
    return v2

sum0 = vecSum([3, 9, -1], [2, 1, 4])
print(sum0)
sum0 = dotProduct([3, 9, -1], [2, 1, 4])
print(sum0)
print(shiftIt([1, 2, 3, 4, 5]))
print(shiftIt([3, 9, -1, 4]))
