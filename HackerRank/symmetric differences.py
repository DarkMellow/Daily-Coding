input()
first_set = set(map(int, input().split()))
input()
second_set = set(map(int, input().split()))

result = first_set ^ second_set
result = list(result)
result.sort()

for i in result:
    print(i)
