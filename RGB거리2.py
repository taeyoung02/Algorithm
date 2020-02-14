n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
'''
0 = 빨 1=초 2=파
첫째집을 하나 정해놓고 시작
나머지는 칠할일 없으므로 큰값으로 놓음
첫째집으로 시작해서 1,2,3째집 칠하는것으로 끝났을때
같은 1번째 집으로 끝나는 경우는 거름
'''

d=[[0]*3 for i in range(n)]
ans=100000000

for i in range(3):
    for j in range(3):
        if i==j:
            d[0][j]=arr[0][i]
        else:
            d[0][j]=1001
    for k in range(1,n):
        d[k][0]=min(d[k-1][1],d[k-1][2])+arr[k][0]
        d[k][1]=min(d[k-1][0],d[k-1][2])+arr[k][1]
        d[k][2]=min(d[k-1][0],d[k-1][1])+arr[k][2]
    for j in range(3):
        if j==i: continue
        ans=min(ans,d[n-1][j])

print(ans)