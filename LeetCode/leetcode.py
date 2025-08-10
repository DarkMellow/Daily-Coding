l = 'baaabbehcbjjjjjllellkk'
m = ''
count = 1


for i in range (0, len(l)):
    if i > 0 and l[i] == l[i-1]:
        count +=1
    else:
        count = 1
            
    if count <= 2:
        m += l[i]
        
print(m)
