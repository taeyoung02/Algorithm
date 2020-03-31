import sys
from collections import deque
t=int(input())

dx=[1,1,-1,-1,2,2,-2,-2]
dy=[2,-2,2,-2,1,-1,1,-1]

def bfs(x,y):
    check[x][y]=0
    q.append((x,y))
    while q:
        (x,y)=q.popleft()
        if x==end_x and y==end_y:
            return check[x][y]
        for i in range(8):
            X=x+dx[i]
            Y=y+dy[i]
            if X>=0 and X<n and Y>=0 and Y<n:
                if check[X][Y]==0:
                    check[X][Y]=check[x][y]+1
                    q.append((X,Y))
                
            
    
for _ in range(t):
    n=int(sys.stdin.readline().strip())
    q=deque()
    check=[[0]*n for _ in range(n)]

    now_x,now_y=map(int, sys.stdin.readline().strip().split())
    end_x,end_y=map(int, sys.stdin.readline().strip().split())

    print(bfs(now_x,now_y))
    