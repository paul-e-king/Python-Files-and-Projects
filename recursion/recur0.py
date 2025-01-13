def pal(w):
    # returns true if w is a palindrome
    x = ""
    if len(w) <= 1:
        return True
    if (len(w) == 2 and w[0] == w[1]):
        return pal("")
    elif (w[0] == w[len(w)-1]):
        if len(w) % 2 == 0:
            for i in range(1, len(w)-1):
                x = x + w[i]
        else:
            for i in range(1, len(w)-1):
                x = x + w[i]
        return pal(x)
    return False

print("racecar: ", pal("racecar"))
print("peer: ", pal("peer"))
print("redivider: ", pal("redivider"))
print("redivvider: ", pal("redivvider"))
print("machine: ", pal("machine"))
print("poop: ", pal("poop"))
print("noon: ", pal("noon"))

