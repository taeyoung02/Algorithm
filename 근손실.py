n,k=map(int,input().split())
kit=list(map(int,input().split()))

kit=[i-k for i in kit]
check=[0]*n
ans=0
def backtracking(sum,cnt):
    if cnt==n:
        global ans
        ans+=1
        return
    
    for i in range(n):
        if (check[i]==False) and (sum+kit[i]>=0):
            check[i]=True
            backtracking(sum+kit[i], cnt+1)
            check[i]=False


backtracking(0,0)
print(ans)