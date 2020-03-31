import sys
sys.setrecursionlimit(10**6)#파이썬 재귀에서 필요
from collections import deque
n=int(input())
arr=[[] for i in range(n)]
for i in range(n):
    a,b = map(int,(input().split()))
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)
stack=[]
circuit=[]
flag=0
def find_circuit(x,pre):
    if x in stack:
        circuit.append(x)
        while True:
            c=stack.pop()
            if c==x:
                return
            else:
                circuit.append(c)

    stack.append(x)
    for i in arr[x]:
        if i!=pre:
            find_circuit(i,x)
            if stack:
                stack.pop()
    return 0
find_circuit(arr[0][0],arr[0][0])

def bfs(x):
    q=deque()
    dist=[0]*n
    q.append(x)
    while q:
        x=q.popleft()
        if x in circuit:
            print(dist[x],end=' ')
            return
        for i in arr[x]:
            if dist[i]==0:
                q.append(i)
                dist[i]=dist[x]+1

for i in range(n):
    bfs(i)
