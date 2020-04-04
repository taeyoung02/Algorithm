from collections import deque
from sys import stdin
n=int(stdin.readline().strip())

adjlist=[[] for i in range(n+1)]

for i in range(n-1):
    a,b=map(int, stdin.readline().strip().split())
    adjlist[a].append(b)
    adjlist[b].append(a)

ans=list(map(int, stdin.readline().strip().split()))
order=[0]*(n+1)
for i in range(n):
    order[ans[i]]=i #입력으로 주어진 정답의 각 노드 순서를 매김


for i in range(1,n+1): #입력으로 주어진 순서를 따르도록 인접행렬을 정렬
    adjlist[i]=sorted(adjlist[i], key=lambda x:order[x])#index함수로 해봤으나 index함수의 시간복잡도가 n만큼임

q=deque()
q.append(1)

check=[0,1]+[0]*(n+1)
result=[1]

def dfs(x):
    check[x]=1
    
    for i in adjlist[x]:
        if check[i]==0:
            result.append(i)
            dfs(i)

dfs(1)

if ans==result:
    print(1)
else:
    print(0)

