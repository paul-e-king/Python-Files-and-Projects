'''
This program will produce pythagorean triples that follow a pattern.
'''

def isOdd(N):
    isO = (N % 2 == 1) and (N >= 3)
    return isO


def makeTriple(N):
    if isOdd(N):
        a = N
        b = ((N//2)*(N+1))
        c = b + 1
        return (a, b, c)
    else:
        return "Error: {} is not an odd number.".format(N)


for i in range(50):
    if isOdd(i):
        t = makeTriple(i)
        print("{}: {:>5}**2 + {:>4}**2 = {:>4}**2".format(t, t[0], t[1], t[2]))