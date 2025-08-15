from random import randint

myList = [randint(1,6) for i in range(50)]
myList.sort()
book = {}

for i in myList:
    if i in book:
        continue
    count = 0
    for j in myList:
        if i == j:
            count += 1
    book[i]=count

frequency = list(book.values())
frequency.sort()
winner = [key for key, value in book.items() if value == frequency[-1]]
print(f'{winner} appeared {frequency[-1]} times')
