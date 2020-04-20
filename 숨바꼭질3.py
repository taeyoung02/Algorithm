from collections import deque
n,k = map(int, input().split())

check=[0]*100001
dist=[0]*100001
stack=[]
def bfs(n,k):
    q=deque()
    check[n]=1
    q.append(n)
    while q:
        x=q.popleft()
        if x==k:
            stack.append(dist[x])
        if x-1>=0:
            if check[x-1]==0:
                q.append(x-1)
                check[x-1]=1
                dist[x-1]=dist[x]+1
            else:
                dist[x-1]=min(dist[x]+1, dist[x-1])
        if x+1<=100000:
            if check[x+1]==0:
                q.append(x+1)
                check[x+1]=1
                dist[x+1]=dist[x]+1
            else:
                dist[x+1]=min(dist[x]+1, dist[x+1])
        if 2*x<=100000:
            if check[2*x]==0:
                q.append(2*x)
                check[2*x]=1
                dist[2*x]=dist[x]
            else:
                dist[2*x]=min(dist[x], dist[2*x])
bfs(n,k)
print(min(stack))