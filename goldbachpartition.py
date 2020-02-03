check=[0,0]+[1]*1000000
for i in range(2,1001):
    if check[i]==True:
        for j in range(2*i,1000001,i):
            check[j]=False



n = int(input())

for i in range(n):
    cnt=0
    a=int(input())
    for i in range(2,int(a/2)+1):
        if check[i] and check[a-i]:
            cnt+=1
    print(cnt)