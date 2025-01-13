ints = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
ends = {"0)", "1)", "2)", "3)", "4)", "5)", "6)", "7)", "8)", "9)"}
inp = input()
arr = inp.split(" ")
op1 = 0
op2 = 0

for i in arr:
    try:
        i = int(i.split(")")[0])
        if i in ints:
            op1 = int(i) + op1
        else:
            op1 = op1 + i
    except: # ignore anything else
        pass

print(op1)
