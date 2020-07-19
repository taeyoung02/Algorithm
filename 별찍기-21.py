import math
n=int(input())

for k in range(n):
    for i in range(math.ceil(n/2)):
        print("*", end=' ')
    print('')
    for j in range(math.ceil((n-1)/2)):
        print("",end=' ')
        print("*",end='')
    print('')