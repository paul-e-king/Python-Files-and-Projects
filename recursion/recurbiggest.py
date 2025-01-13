def find(arr):
    highest = -1
    hi2 = -1
    if len(arr) == 1:
        return highest
    else:
        highest = arr[0]
        hi2 = find(arr[1:len(arr)])
        if highest < hi2:
            return hi2
        else:
            return highest

arr0 = [55, 10, 97, 6, 100, 75, 63]
print("The highest number is: ", find(arr0))
