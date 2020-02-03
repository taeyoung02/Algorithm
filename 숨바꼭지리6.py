n,s=map(int,input().split())

a=list(map(int,input().split()))

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
if n==1:
    print(abs(a[0]-s))
    exit(0)
v=gcd(abs(a[0]-s),abs(a[1]-s))
for i in range(2,n):
    v=gcd(v,abs(a[i]-s))

print(v)