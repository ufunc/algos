def ternary_search(arr, target, low, high):
    if high >= low:

        mid1 = low + (high - low) // 3
      
        mid2 = high - (high - low) // 3
      

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

  
        elif target < arr[mid1]:
            return ternary_search(arr, target, low, mid1 - 1)

        elif target > arr[mid2]:
            return ternary_search(arr, target, mid2 + 1, high)

        else:
            return ternary_search(arr, target, mid1 + 1, mid2 - 1)

    return -1
