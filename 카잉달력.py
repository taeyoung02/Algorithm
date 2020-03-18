n=int(input())

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

for _ in range(n):
    M,N,x,y=map(int,input().split())
    ans=0
    if (x==M)and(y==N):
        print(M*N//gcd(M,N))
        continue
    for i in range(y,M*N//gcd(M,N)+1,N):
        if (i-x)%M == 0:
            ans=i
            print(ans)
            break
    if ans==0:
        print(-1)