from collections import deque
import sys
n=int(input())
arr=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

check=[[0]*n for i in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(i,j,cnt):
    check[i][j]=1
    q=deque()
    q.append((i,j))
    while q:
        x,y=q.popleft()
        arr[x][y]=cnt
        for i in range(4):
            X=x+dx[i]
            Y=y+dy[i]
            if 0<=X<n and 0<=Y<n and check[X][Y]==0 and arr[X][Y]==1:
                check[X][Y]=1#꺼낼때 방문표시를 하는게아니라 넣을때 방문표시를 해야 for문에서 중복 방문이 안일어남
                q.append((X,Y))
cnt=1
for i in range(n):
    for j in range(n):
        if check[i][j]==0 and arr[i][j]==1:
            bfs(i,j,cnt)
            cnt+=1
dist=[[-1]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            dist[i][j]=0
ans=10000000
q=deque()
for i in range(n):
    for j in range(n):
        if arr[i][j]!=0:
            q.append((i,j))
while q:
    x,y=q.popleft()
    for k in range(4):
        X=x+dx[k]
        Y=y+dy[k]
        if 0<=X<n and 0<=Y<n:
            if dist[X][Y]==-1:
                arr[X][Y]=arr[x][y]
                dist[X][Y]=dist[x][y]+1
                q.append((X,Y))
            elif arr[X][Y]!=arr[x][y]:
                ans=min(ans,dist[x][y]+dist[X][Y])
print(ans)