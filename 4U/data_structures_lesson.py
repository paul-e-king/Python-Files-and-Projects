# treat a list as a set
a = [3, 5, 1, 2, 5, 5]
for i in range(10):
    if i in a:
        print(i, "is in a")
    else:
        print(i, "is not in a")
print(a)

b = {6, 9, 4, 7}
for i in range(10):
    if i in b:
        print(i, "is in b")
    else:
        print(i, "is not in b")
print(b)
for s in b:
    print(s, end=" ")
print("\n", len(b))

c = set(a)
print(c | b)
print(c & b)
if (c & b == set({})):
    print("intersection of b and c is the empty set")
    
autos = {"Ford":"Escort", "Volvo":"XC6", "Toyota":"Camry", "Jeep":"Grand Cherokee", "Chevrolet":"Corvette", "GM":"Cadillac"}
makes = []
for key in autos:
    makes.append(key)
print(makes)
for m in makes:
    print(autos[m])

for key in autos:
    print(key, "=>", autos[key])

myPrimes = (2, 3, 5, 7, 11, 13, 17, 29)
if 23 not in myPrimes:
    print("23 is missing from ", myPrimes)

print(myPrimes[:4])
print(myPrimes[5:])
print(myPrimes[2:6])
print(myPrimes[-1])
