n, sum = int(input("Num: ")), 0
mylist, lower_list = [], []
for i in range(1, int(n**0.5) + 1):
    if n%i == 0:
        mylist.append(i)
for i in mylist:
    lower_list.append(n//i)
lower_list.sort()
mylist.extend(lower_list), mylist.pop()
print(mylist)

for i in mylist:
    sum += i
print(f"Sum: {sum}")
if sum == n:
    print(True)
else:
    print(False)
