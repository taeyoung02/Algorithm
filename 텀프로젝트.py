import sys
sys.setrecursionlimit(111111)#필수
test=int(input())
def dfs(x,start,check,arr):
    global cnt
    check[x]=1
    y=arr[x-1]
    if check[y]==0:
        return dfs(y,start,check,arr)
    else:
        while start!=y:
            start=arr[start-1]
            cnt+=1

for _ in range(test):
    n=int(input())
    arr=list(map(int, sys.stdin.readline().strip().split()))
    cnt=0
    check=[0]*(n+1)
    ans=0
    for i in range(1,n+1):
        if check[i]==0:
            dfs(i,i,check,arr)
    print(cnt)

             
           