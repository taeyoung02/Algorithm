n=int(input())
sign=list(input().split())
ansarr=[]
check=[0]*10
def go(numarr,cnt):
    if cnt==n:
        ansarr.append(numarr)
        return
    
    if sign[cnt]=='>':
        for i in range(0,10):
            if numarr[cnt]>i and check[i]==0:
                check[i]=1
                go(numarr+[i],cnt+1)
                check[i]=0
    if sign[cnt]=='<':
        for i in range(0,10):
            if numarr[cnt]<i and check[i]==0:
                check[i]=1
                go(numarr+[i],cnt+1)
                check[i]=0
for i in range(0,10):
    check[i]=1
    go([i],0)
    check[i]=0
ansarr.sort()
for i in ansarr[-1]:
    print(i,end='')
print()
for i in ansarr[0]:
    print(i,end='')