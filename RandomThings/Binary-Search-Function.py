
def Binary_Search_Algorithm(myList, query):
    myList.sort()
    lower_limit = 0
    upper_limit = len(myList)-1

    while lower_limit <= upper_limit:
        midpoint = (lower_limit+upper_limit)//2
        midelement = myList[midpoint]

        if midelement == query:
            return midpoint
        elif midelement < query:
            lower_limit = midpoint+1
        elif midelement > query:
            upper_limit = midpoint-1

myList = list(map(int, input().split()))
print(f"{myList} <{len(myList)}>")
query = int(input("Query: "))

print(f"Index: {Binary_Search_Algorithm(myList, query)} -> {query}")