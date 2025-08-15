def missingNumber(arr):
    arr = sorted(list(set(arr)))
    if not arr:
        return 1
    if arr[0] != 1:
        return 1
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        # If arr[mid] == mid + 1, then missing number is in right half
        if arr[mid] == mid + 1:
            left = mid + 1
        else:
            # Missing number is in left half (or found)
            right = mid - 1
    # At this point, left is the index where missing number should be
    return left + 1

test = [1,2,3,4,6,7,8,9,10]
result = missingNumber(test)
print(f"Test: {test} -> Missing: {result}")