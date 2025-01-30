def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [1, 5, 9, 10, 14, 19]
target = 19
result = linear_search(arr, target)
print(result)
