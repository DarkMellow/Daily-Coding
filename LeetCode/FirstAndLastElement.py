from random import randint

def LocationTracker(nums, target, mid, direction):
    if direction == 'start':
        midelement = nums[mid]
        if midelement == target:
            if mid-1 >= 0 and nums[mid-1] == target:
                return 'left'
            else:
                return 'found'
        elif target < midelement:
            return 'left'
        else:
            return 'right'
    elif direction == 'end':
        midelement = nums[mid]
        if midelement == target:
            if mid-1 >= 0 and nums[mid+1] == target:
                return 'right'
            else:
                return 'found'
        elif target < midelement:
            return 'left'
        else:
            return 'right'

def BinarySearch(nums, target):
    lower = 0
    upper = len(nums) - 1
    leftside = None
    rightside = None
    side = 'start'
    while lower <= upper:
        mid = (lower+upper)//2
        result = LocationTracker(nums, target, mid, side)
        if result == 'found':
            leftside = mid
            break
        elif result == 'left':
            upper = mid - 1
        elif result == 'right':
            lower = mid + 1
    else:
        leftside = -1
    side = 'end'
    lower = 0
    upper = len(nums) - 1
    while lower <= upper:
        mid = (lower+upper)//2
        result = LocationTracker(nums, target, mid, side)
        if result == 'found':
            rightside = mid
            break
        elif result == 'left':
            upper = mid - 1
        elif result == 'right':
            lower = mid + 1
    else:
        rightside = -1

    return [leftside, rightside]

myStack = [randint(1,10) for i in range(30)]
myStack.sort()
print(myStack)

searchFor = int(input("Search : "))
final = BinarySearch(myStack, searchFor)

print(f'Found -> {final}')