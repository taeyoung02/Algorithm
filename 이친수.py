n=int(input())
if n==1:
    print("1")
    exit(0)
d=[[0]*2 for i in range(n+1)]
d[1][1]=1
d[2][0]=1

for i in range(3,n+1):
    for j in range(2):
        if j==1:
            d[i][j]=d[i-1][0]
        else:
            d[i][j]=d[i-1][0]+d[i-1][1]

print(d[n][0]+d[n][1])