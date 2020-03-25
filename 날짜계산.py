e,s,m=map(int, input().split())
e-=1
s-=1
m-=1
for i in range(0,15*28*19+1):
    if i%15==e:
        if i%28==s:
            if i%19==m:
                print(i+1)
                exit(0)
