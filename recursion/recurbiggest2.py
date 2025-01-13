def find(arr):
    highest = arr[0]
    hi2 = ""
    if len(arr) == 1:
        return highest
    else:
        hi2 = find(arr[1:len(arr)])
        if highest < hi2:
            return hi2
        else:
            return highest

# arr0 = [55, 10, 97, 6, 100, 75, 63]
arr0 = ["delta", "charlie", "echo", "alpha", "bravo"]
print("The highest value is: ", find(arr0))
