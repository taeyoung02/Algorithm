n, m=map(int,(input().split()))
arr=list(map(int,input().split()))
#비트마스크
#[a,b,c,d]에서 1011 = a,c,d 이다
cnt=0
for i in range(1,1<<n):#2의n제곱-1 까지 검사
    sum=0
    for j in range(n):#1 10 100 1000 1000 검사할거임(arr의 몇번째 원소가 있는지)
        if i&(1<<j):
            sum+=arr[j]
    if sum==m:
        cnt+=1
print(cnt)