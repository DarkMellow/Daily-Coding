from random import randint

def LocationTracker(stack, thief, mid):
    midelement = stack[mid]
    if midelement == thief:
        if mid-1 >= 0 and stack[mid-1] == thief:
            return 'left'
        else:
            return 'found'
    elif midelement < thief:
        return 'right'
    else:
        return 'left'

def BinarySearch(stack, thief):
    lower_limit, upper_limit = 0, len(stack)-1
    
    while lower_limit <= upper_limit:
        mid = (lower_limit+upper_limit)//2
        result = LocationTracker(stack, thief, mid)

        if result == 'found':
            return mid
        elif result == 'right':
            lower_limit = mid+1
        elif result == 'left':
            upper_limit = mid-1

myStack = [randint(1,6) for i in range(10)]
myStack.sort()
print(myStack)

query = int(input("Query: "))
outcome = BinarySearch(myStack, query)
print(f"{query} found first at index : {outcome}")