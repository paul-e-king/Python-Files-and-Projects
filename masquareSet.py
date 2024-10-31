"""
Magic square program

This is by no means a model solution to the ICS4U assignment. In this code, 
I don't check for primes (or if at least 3 and 2 are not factors of the
array dimension); I don't check for magic. I am confident it meets the basic
specs if N is prime, or if 2 and 3 are not factors of the array dimension, 
but I wouldn't give myself a level 4 for this one.

It means that the usual primes will work: 5, 7, 11, 13, 17, 19, and higher
primes. Also, 35, 55, 65, 77, and so on because they are the products of
previously working primes (which don't have 2 and 3 as factors). In other words,
it works for the general case, but I don't manage user input to ensure proper
input, so non-magic squares may result for bad user input.

Comments are sparse and should state a purpose. You don't know it's me coding
it, and there is no variable dictionary (or it is extremely minimal).
"""
import random as r

def shakeup(A):
    # Shuffles a list of numbers.
    #
    # preconditions: A is a list (1D)
    # postcondition: A is the same list in scrambled order
    n = 0
    for i in range(len(A)):
        idx = r.randrange(0, len(A))
        temp = A[i]
        A[i] = A[idx]
        A[idx] = temp
    return A

def mkArr(A, shift):
    # Creates a 2D array given a 1D array and a shift value.
    #
    # preconditions: A is a shuffled list and shift is the value to shift in a 2D array
    # postcondition: A 2D array of shifted numbers (a semi-magic square)
    dim = len(A)
    A2 = []
    for i in range(dim):
        A2.append([0] * dim)
    A2[0] = A
    lower = dim - shift
    upper = lower + dim
    for i in range(1, dim):
        count = 0
        for j in range(lower, upper):
            A2[i][count] = A2[i-1][j % dim]
            count += 1

    return A2

def add(A, B):
    # Returns a new matrix which is the sum of A and B.
    #
    # precondition: A and B are square matrices of the same dimensions
    # postcondition: Return the matrix sum of A + B, which should be magic
    #      if the conditions are right.
    matSum = [0] * len(A)
    oneRow = []
    for i in range(len(A)):
        matSum[i] = [[0] * len(A)]
        oneRow = [0] * len(A)
        for j in range(len(A)):
            oneRow[j] = A[i][j] + B[i][j]
        matSum[i] = oneRow
    
    return matSum

# The main Driver code:
#
dim = 0
arr = []
arr0 = []
while dim < 5:
    dim = int(input("Enter a dimension > 3: "))

print("Magic number for N=%d will be = %d" %(dim, ((dim**2)*(1+dim**2)/(dim*2))))
for i in range(dim):
    arr.append(i+1)
    arr0.append(i * dim)

arr = shakeup(arr)
arr0 = shakeup(arr0)
arr2 = mkArr(arr, 2)
arr3 = mkArr(arr0, 3)
for a in arr2:
    print(a)
for a in arr3:
    print(a)
arrSum = add(arr2, arr3)

print()
for i in range(len(arrSum)):
    for j in range(len(arrSum)):
        print("%4d " % arrSum[i][j], end="")
    print()
print()

