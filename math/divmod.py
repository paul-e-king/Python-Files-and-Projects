print("This program performs the division p / q")
p = int(input("Enter p: (a whole number): "))
q = int(input("Enter q: (a whole number): "))
div = p // q
mod = p % q
print("%d goes %d times into %d" % (q, div, p))
print("the remainder is %d" % mod)
