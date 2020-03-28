n=int(input())

arr=[list(map(int,input().split())) for _ in range(n)]
ans=100000000
    
def go(i,first,second):
    if i==n:
        global ans
        (a,b)=(0,0)
        for i in first:
            for j in first:
                a+=arr[i][j]
        for i in second:
            for j in second:
                b+=arr[i][j]
        ans=min(abs(a-b),ans)
        return
    
    go(i+1,first+[i],second)
    go(i+1,first,second+[i])

go(1,[0],[])
print(ans)
