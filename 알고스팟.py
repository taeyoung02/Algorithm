from collections import deque
n, m=map(int,(input().split()))
arr=list(list(map(int,list(input()))) for _ in range(m))
check=[[0]*n for _ in range(m)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
dist=[[0]*n for _ in range(m)]
#덱 사용. 가중치가 0인건 앞에, 1인건 뒤에 추가하여 가중치가 낮은거부터 순회
def bfs(n,m):
    q=deque()
    q.append((0,0))
    while q:
        x,y=q.popleft()
        if (x,y)==(n,m):
            return dist[x][y]
        for i in range(4):
            X=x+dx[i]
            Y=y+dy[i]
            if 0<=X<=n and 0<=Y<=m and check[X][Y]==0:
                check[X][Y]=1
                if arr[X][Y]==0:
                    q.appendleft((X,Y))
                    dist[X][Y]=dist[x][y]
                elif arr[X][Y]==1:
                    q.append((X,Y))
                    dist[X][Y]=dist[x][y]+1
n,m=m,n 
print(bfs(n-1,m-1))