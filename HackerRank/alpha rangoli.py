size = int(input("Enter a number between 5-25 : "))

alpha = [chr(i) for i in range(97,97+size)] #Converting ascii into alphabets
alpha.reverse()
alpha.extend(alpha[-2::-1])
width = len('-'.join(alpha))

# First Half of the pyramid till the centre
for i in range(1,size+1):
    left = alpha[:i]
    right = alpha[-1:-i:-1]
    right.reverse()
    print('-'.join(left+right).center(width,'-'))

# Bottom Half of the pyramid 
for i in range(size-1,0,-1):
    left = alpha[:i]
    right = alpha[-1:-i:-1]
    right.reverse()
    print('-'.join(left+right).center(width,'-'))

