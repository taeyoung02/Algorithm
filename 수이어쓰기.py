n=int(input())
length=0
for i in range(1,10):
    if n<10**i:
        print(length+i*(n-(10**(i-1)))+len(str(n)))
        exit(0)
    else:
        length+=i*(10**i-(10**(i-1)))
