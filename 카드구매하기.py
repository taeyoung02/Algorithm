n=int(input())
p=list(map(int,input().split()))
d=p
for i in range(n):
    for j in range(i):
        d[i]=max(d[i],d[i-j-1]+p[j])
print(d[n-1])