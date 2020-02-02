N, K = map(int,input().split())
A=[list(map(int, input().split())) for i in range(N)]

K, M = map(int,input().split())
B=[list(map(int, input().split())) for i in range(K)]



res=[[0]*M for i in range(N)]

for n in range(N):
    for m in range(M):
        for k in range(K):
            res[n][m]+=A[n][k]*B[k][m]

for n in range(N):
    for m in range(M):
        print(res[n][m], end=' ')
    print()


