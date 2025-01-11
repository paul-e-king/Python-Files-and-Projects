# This is a look at sets. 
# Unlike lists, sets have an order, regardless of the order the elements
# were inserted.
#
# Sets can't be accessed by index value or hash. But you can test if a value
# exists by using the "in" keyword, and  you can traverse the set by using
# a for loop in the manner given below.
#

s = set({}) # without casting, Python assumes this is a dictionary

def mkSet(S, n):
    if n not in S:
        S.add(n)
    else:
        print(n, " is already in the set.")
    return S

for i in range(10):
    mkSet(s, i)

print(s)

T = {12, 11, 10, 7, 8, 9, 13, 14, 15}
U = s | T # Union of s and T
for x in U:
    print(x, " ", end="")
print()

V = s & T # intersection of s and T
for x in V:
    print(x, "<<- intersection ", end="")
print()

if U.issuperset(s):
    print("U contains s")

if U.issuperset(T):
    print("U contains T")

if U.issuperset(V):
    print("U contains V")

X = s | T | V | {999, 998, 997}
print("Union of S, T, V, and a fourth set:")
for x in X:
    print(x, end=" ")
print()

if U > s and U > T and U > V:
    print("U is the universal set")

if X > U:
    print("X contains U")

W = {88, 89, 90, 91}
empty = set({}) # the empty set
if empty == U & W:
    print ("U and W are mutually exclusive")

if U.isdisjoint(W): # logically the same as the above IF
    print ("U and W are mutually exclusive")
else:
    print("There is at least one element in U that is in W")

if {9} == U & W: # something not empty
    print ("testing of mutual exclusion failed")
else:
    print("this is the only message you should see")

A = {0, 1, 2}
B = A
if A <= B and B <= A: # <= means "is a subset of" (not a proper subset)
    print("A and B are the same set")

if A.isdisjoint(B): 
    print("A and B have no elements in common")
else: # there are a number of possibilities, so we'll go with ...
    print("There is at least one element in A that is in B")
