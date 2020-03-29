n, m=map(int,(input().split()))
arr=[list(map(int,list(input()))) for _ in range(n)]#list를 씌우면 str이 한개씩 나눠서 저장됨

ans=0
for i in range(1<<(n*m)):
    sum=0
    for j in range(n):
        cur=0
        for k in range(m):
            if i&(1<<(m*j+k)):
                cur*=10
                cur+=arr[j][k]
            else:
                sum+=cur
                cur=0
        sum+=cur

    for j in range(m):
        cur=0
        for k in range(n):
            if i&(1<<(k*m+j))==0:
                cur*=10
                cur+=arr[k][j]
            else:
                sum+=cur
                cur=0
        sum+=cur
    ans=max(ans,sum)

print(ans)