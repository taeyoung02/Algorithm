from collections import deque
n,k = map(int, input().split())

check=[0]*100001
dist=[0]*100001
def bfs(n,k):
    q=deque()
    check[n]=1
    q.append(n)
    while q:
        x=q.popleft()
        if x==k:
            return dist[x]
        if 100001>x-1>=0 and check[x-1]==0:
            q.append(x-1)
            check[x-1]=1
            dist[x-1]=dist[x]+1
        if 0<=x+1<100001 and check[x+1]==0:
            q.append(x+1)
            check[x+1]=1
            dist[x+1]=dist[x]+1
        if 0<=2*x<100001 and check[2*x]==0:
            q.append(2*x)
            check[2*x]=1
            dist[2*x]=dist[x]+1

print(bfs(n,k))