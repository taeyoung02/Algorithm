test=int(input())

for _ in range(test):
    a,b=map(int,input().split())

    
    sqrt_a=a%10
    sqrt=[sqrt_a]
    for i in range(b):
        sqrt_a=(sqrt_a*a)%10
        if sqrt_a in sqrt:
            break
        sqrt.append(sqrt_a)
    for i in range(len(sqrt)):
        if sqrt[i]==0:
            sqrt[i]+=10
    print(sqrt[b%len(sqrt)-1])