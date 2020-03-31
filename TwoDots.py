n,m=map(int,input().split())

arr=[input() for _ in range(n)]
check=[[0]*m for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y,cnt,pre_xy):
    if check[x][y]==1:
        if cnt>=4:
            return 1
        else:
            return 0
    
    check[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and (arr[nx][ny]==arr[x][y]) and pre_xy!=(nx,ny):
            if dfs(nx,ny,cnt+1,(x,y)):
                return 1

    return 0

for i in range(n):
    for j in range(m):
        if check[i][j]==0:
            ans=dfs(i,j,0,(0,0))
        if ans==1:
            print('Yes')
            exit(0)
print('No')
