import math
import time
import sys

def getInt(prompt):
    valid = False
    while not valid:
        try:
            N = int(input(prompt))
            valid = True
        except:
            print("Data type error. Please enter a whole number.")
    return N

silent = False
if len(sys.argv) > 1:
    argv = sys.argv[1]
    silent = (argv == "-s")
    print("Silent mode")

count = 0
num = getInt("Please enter a whole number: ")
start_time = time.time()
max0 = math.floor(math.sqrt(num))
for i in range(1, max0 + 1):
    if num % i == 0:
        if not silent:
            print(f'{i:,}', end="\t")
            fac2 = num // i
            print(f'{fac2:,}')
        count += 2

if count > 2:
    print(f"Number of factors of {num:,}: {count:,}")
else:
    print("%d is prime." % num)

elapsed = time.time() - start_time
print("Execution in %.5f seconds." % elapsed)

