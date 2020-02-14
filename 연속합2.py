n=int(input())
arr=list(map(int,input().split()))

d1=[0]*n
d2=[0]*n
d1[0]=arr[0]
d2[n-1]=arr[n-1]
for i in range(1,n):
    d1[i]=arr[i]
    if d1[i]<d1[i-1]+arr[i]:
        d1[i]=d1[i-1]+arr[i]

for i in range(n-2,-1,-1):
    d2[i]=arr[i]
    if d2[i]<d2[i+1]+arr[i]:
        d2[i]=d2[i+1]+arr[i]
ans=max(d1)
if n<3:
    print(ans)
    exit(0)
res=[0]*(n-2)
for i in range(1,n-1):
    res[i-1]=d1[i-1]+d2[i+1]

print(max([max(res),ans]))