s1=list(input())
s2=list(input())
d=[[0]*1001 for i in range (1001)]
def solve(a, b):
    if a >= len(s1) or b>=len(s2):
        return 0
    if s1[a]==s2[b]:
        return 1+solve(a+1,b+1)
    if d[a][b]!=-1:
        return d[a][b]
    d[a][b]=max(solve(a+1,b),solve(a,b+1))
    return d[a][b]

Ret=solve(0,0)
print(Ret)
