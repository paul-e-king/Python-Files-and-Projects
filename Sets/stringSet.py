# This is a look at sets. 
# Unlike lists, sets have an order, regardless of the order the elements
# were inserted.
#
# Since magic squares rely on a scrambling of numbers, sets are not really a 
# good choice.

def mkSet(n):
    S = set({})
    S.add("keyboard")
    S.add("bottle")
    S.add("dish")
    S.add("aardvark")
    return S

s = mkSet(5)
print(s)
if ("zebra" not in s):
    s.add("zebra")
    print(s)

if ("aardvark" not in s):
    s.add("aardvark")
    print(s)
else:
    print("aardvark is already in the set")
