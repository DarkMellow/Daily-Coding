# Question 1: Removing Duplicates
myList = []
number = int(input())
for i in range(number):
    element = input()
    myList.append(element)
mySet = set(myList)
print(len(mySet))


#Question 2: Random Operations on a Set
input()
mySet = set(map(int, input().split()))
operation = int(input())
for i in range(operation):
    task = input().split()
    if task[0] == 'remove':
        mySet.remove(int(task[1]))
    elif task[0] == 'pop':
        mySet.pop()
    elif task[0] == 'discard':
        mySet.discard(int(task[1]))
print(sum(mySet))