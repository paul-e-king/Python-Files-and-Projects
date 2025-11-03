def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Example usage
numbers = [10, 23, 45, 70, 11, 15]
target = 70

result = linear_search(numbers, target)
if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")
