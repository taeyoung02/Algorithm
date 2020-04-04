def setting():
    import sys
    from collections import deque
    sys.setrecursionlimit(10**6)#파이썬 재귀에서 필요

    n=int(input())
    arr=[[] for i in range(n)]

    for i in range(n):
        a,b = map(int,(input().split()))
        arr[a-1].append(b-1)
        arr[b-1].append(a-1)

    check=[0]*n
    dist=[0]*n #순환선으로부터의 거리
    q=deque()
    return n,arr,check,dist,q

def find_circuit(x,pre):
    if check[x]==1:#순환 첫 요소 찾음
        return x
    
    check[x]=1
    for i in arr[x]:
        if i==pre:
            continue
        res=find_circuit(i,x)
        #첫 요소 방문 뒤
        if res>=0:#방금 방문한 노드의 리턴값
            check[x]=2#현재 노드는 사이클이다
            if res==x:#다시 돌아 첫노드로 돌아왔을때
                return -2 #이제부턴 방문했지만 사이클은 아니다
            else: return res #아직 사이클 방문중
    return -1
def set_dist(q):
    for i in range(n):
        if check[i]==2:
            dist[i]=0
            q.append(i)
        else:
            dist[i]=-1
    return q

def bfs(q):
    while q:
        x=q.popleft()
        for i in arr[x]:
            if dist[i]==-1: #아직 방문안된 노드는
                q.append(i)#다음으로 간다
                dist[i]=dist[x]+1#거리는 순환선으로부터 1증가 맨처음실행시엔 dist[x]=0이고(순환선) 다음엔 비순환선이 들어감

def ans():
    for i in range(n):
        print(dist[i],end=' ')

if __name__ == "__main__":
    n,arr,check,dist,q=setting()
    find_circuit(0,-1)
    bfs(set_dist(q))
    ans()
    
