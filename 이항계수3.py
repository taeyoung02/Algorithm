# n C k = n! / k!(n-k)!
# n C k를 1000000007로 나눈 나머지를 구하라 (n,k는 매우큼)
n,k=map(int,input().split())
p=1000000007
facN=1
facN_K=0
facK=0
for i in range(2,n+1):
    facN=facN*i%p
    if i==n-k:
        facN_K=facN
    elif i==k:
        facK=facN
def requr(n,k):
    if k==0:
        return 1
    temp=requr(n,int(k/2))
    result=temp*temp%p
    if k%2:
        result*=n
    return result%p
print(facN*requr(facN_K,p-2)%p*requr(facK,p-2)%p)


'''
페르마의 소정리

a**(p-1)=1 (mod p)

a**(p-2)=a**-1 (mod p)

[n! / k!(n-k)!] (mod p) = [n! * ( k!(n-k)! )**(p-2)] (mod p)

= [n! * k!**(p-2)(mod p) * (n-k)!**(p-2)(mod p)]