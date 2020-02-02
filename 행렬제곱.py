n,b=map(int, input().split())
A=[list(map(int, input().split())) for i in range(n)]

def requr(k):
    if k==1:
        return [[x%1000 for x in l] for l in A]
    temp=requr(int(k/2))
    result=matmul(temp,temp)
    if k%2:
        result=matmul(A,result)
    return [[x%1000 for x in l] for l in result]
def matmul(a,b):
    mat=[[0]*n for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                mat[k][i]+=a[k][j]*b[j][i]
    return mat

result=requr(b)
for i in result:
    for j in i:
        print(j,end=" ")
    print()