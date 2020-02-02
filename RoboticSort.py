import sys
while True:
    a=[]
    n=int(sys.stdin.readline().rstrip())
    if n==0:
        break
    a=list(map(int,sys.stdin.readline().split()))
    for i in range(n):
        a[i]=(a[i],i)

    for i in range(n):
        print(a.index(i+1)+1)
        for j in range(n):
            a[i]