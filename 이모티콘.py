from collections import deque
k = int(input())

dist=[[0]*2001 for i in range(2001)]
def bfs(ans):
    q=deque()
    dist[1][0]=0
    q.append((1,0))
    while q:
        s,c=q.popleft()
        if s==ans:
            return dist[s][c] 
        if s!=0 and dist[s-1][c]==0:
            q.append((s-1,c))
            dist[s-1][c]=dist[s][c]+1
        if c!=0 and dist[s+c][c]==0:
            q.append((s+c, c))
            dist[s+c][c]=dist[s][c]+1
        if s!=0 and dist[s][s]==0:
            q.append((s,s))
            dist[s][s]=dist[s][c]+1

print(bfs(k))