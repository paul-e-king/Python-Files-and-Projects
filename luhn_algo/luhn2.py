# This code earned 100/100 (5/5 pts) in the ECOO '13 R1 P2: The Luhn Algorithm,
# according to DMOJ (dmoj.ca).
#
# I have tested this code against my bank cards and credit cards, and it has worked
# well each time. 

def reverse(S):
    # S is a number, as string.
    # rev is the returned number with the digits reversed, also a string.
    #
    # We need to reverse S. One problem is to watch that a number with a trailing 
    # zero is returned as a number with a leading zero, and vice versa.
    # There also might be multiple trailing zeroes, or multiple leading zeroes.
    # Purpose: Reversing a string makes it easier to think about how
    #          to program a checksum, by moving forward instead of backward.
    #
    # Warning: The input string MUST be the same LENGTH as the returned string.
    # Example: 1230 to be returned as the string 0321, not 321
    # Example: 0123 to be returned as the string 3210
    # Example: 4567000 to be returned as the string 0007654, not 7654
    #
    # The simple solution would have been to keep everything as string, but I 
    # thought I'd have fun with working with integer.
    #
    length = len(S)
    S = int(S) # Temporarily change this to an integer
    addback = (S % 10 == 0) 
    rev = 0
    while S != 0:
        digit = S % 10
        rev = (rev * 10) + digit
        S = S // 10
    # we will return a string
    if addback: # if the original string ended with 0, add it to the start.
        num0s = length - len(str(rev))   # How many zeroes do we need?
        # convert rev to string using the necessary number of zeros
        rev = ('0' * num0s) + str(rev)
    else:
        rev = str(rev)
    return rev 

def numize(N):
    # simply returns the sum of digits, via Luhn algorithm
    sum0 = 0
    for i in range(len(N)-1):
        Nb = reverse(N) # allows us to move forward in the string
        # print("%s <- $s" % N, Nb)
        if i % 2 == 1:
           dS = 2 * int(Nb[i])
           if dS >= 10:
               dS = dS - 9
               sum0 = sum0 + dS
           else:
               sum0 = sum0 + dS
        else:
           dS = int(Nb[i])
           sum0 = sum0 + dS
    return sum0

##### Driver code
inp = ""
# 5 test cases per line in 5 lines
tot = 0
tot2 = 0
checkd = 0
file0 = "luhn.dat"
fh = open(file0, "r")
numdat = 3
for i in range(1, numdat+1):
    inp = fh.readline() # one line of 5 numbers read
    inp = inp[:-1] # trim the newline
    valid = numize(inp) % 10
    print(numize(inp), " ", end="")
    if not (valid == 0):
        print("%d: %s is not a valid CC number (%d)" % (i, inp, valid))
    else: 
        print("%d: %s is valid (%d)" % (i, inp, valid))
    
    
