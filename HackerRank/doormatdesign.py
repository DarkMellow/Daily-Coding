x = input().split()

# Just put two inputs with a space and it will do the trick, make sure to do [x 3x]
design = '.|.'
for i in range(1,int(x[0]),2):
    print((design*i).center(int(x[1]),'-'))
print("WELCOME".center(int(x[1]), '-'))
for i in range(int(x[0])-2,0,-2):
    print((design*i).center(int(x[1]),'-'))

