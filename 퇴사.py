n=int(input())
t=[0]*n
p=[0]*n
for i in range(n):
    t[i],p[i]=map(int,(input().split()))
ans=0
def go(n, cur, money):
    global ans
    if n==cur:
        ans=max(money,ans)
        return
    
    if n>=cur+t[cur]:
        go(n, cur+t[cur],money+p[cur])
    go(n,cur+1,money)

go(n,0,0)
print(ans)