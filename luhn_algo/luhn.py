# This code earned 100/100 (5/5 pts) in the ECOO '13 R1 P2: The Luhn Algorithm,
# according to DMOJ (dmoj.ca).
#
# I have tested this code against my bank cards and credit cards, and it has worked
# well each time. 

def reverse(S):
    # S is a string
    # returns rev, the reverse, which is another string
    rev = ""
    for c in range(len(S)-1, -1, -1):
        # print ("reverse: ", c)
        rev = rev + S[c]

    return rev 

def luhnAdd(N):
    # simply returns the sum of digits, via Luhn algorithm
    total = 0
    for i in range(len(N)):
        if (i % 2 == 1):
            t = 2*int(N[i])
            if t >= 10:
                t = t - 9 # same effect as adding the digits
            total = total + t
            # print("Double: ", t, " total = ", total)
        else:
            total = total + int(N[i])
            # print("add: ", int(N[i]), " total = ", total)
    return total

##### Driver code
file = "luhn.dat"

with open(file, "r") as fh:
    for n in fh:
        n = n[:-1]
        rev = reverse(n)
        tot = luhnAdd(rev) # remove newline
        valid = (tot % 10 == 0)
        if valid:
            print(tot, "Valid", n)
        else:
            print(tot, "not Valid", n)

fh.close()
