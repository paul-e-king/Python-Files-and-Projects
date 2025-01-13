# This code checks for different array types
a = [9, 12, 7, 2, 11, 5]
b = (2, 3, 6, 5, 1)
c = {"brand": "Ford", "model": "Mustang", "year": 1964}
d = 5
for i in [a, b, c, d]:
    if isinstance(i, list):
        print("This is a list")
    elif isinstance(i, tuple):
        print("This is a tuple")
    elif isinstance(i, dict):
        print("This is a dictionary")
        print(c["year"])
    else:
        print("not sure")
