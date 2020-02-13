n = int(input())
a=[]
for i in range(n):
    a.append(int(input()))

d=[[0]*4 for i in range(100001)]
d[1][1]=1
d[2][2]=1
d[3][1]=1
d[3][2]=1
d[3][3]=1
for i in range(4,100001):
    for j in range(1,4):
        if j==1 and i>=j:
            d[i][j]=d[i-j][2]+d[i-j][3]
        if j==2 and i>=j:
            d[i][j]=d[i-j][1]+d[i-j][3]
        if j==3 and i>=j:
            d[i][j]=d[i-j][1]+d[i-j][2]
        d[i][j]%= 1000000009
for t in range(n):
    sum=0
    for i in range(1,4):
        sum+=d[a[t]][i]
    print(sum% 1000000009)
