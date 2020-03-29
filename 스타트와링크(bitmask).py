n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

ans=1000000000
for i in range(1<<n):
    first=[]
    second=[]
    for j in range(n):
        if i&(1<<j):
            first.append(j)
        else: second.append(j)
    if len(first)==n/2 and len(second)==n/2:
        sum1=0
        sum2=0
        for i in first:
            for j in first:
                sum1+=arr[i][j]
        for i in second:
            for j in second:
                sum2+=arr[i][j]
    
        ans=min(ans,abs(sum1-sum2))
print(ans)