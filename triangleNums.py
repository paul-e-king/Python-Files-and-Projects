"""
This code is intended to be a corrected version of a similar question from the 
test item bank
"""
n = 1
t = 0
max = 6

while (n <= max):
    t = t + n
    print("%d" % (n), end="", sep="")
    if (n < max):
        print(" + ", end="", sep="")
    n += 1

print(" = %d" % t)
