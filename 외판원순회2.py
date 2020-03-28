from itertools import permutations
n = int(input())
cost= [list(map(int, input().split())) for _ in range(n)]

order = [i for i in range(n)]

order_sum=list(permutations(order[1:n]))
ans=100000000
for i in order_sum:
    i=list(i)
    i.append(order[0])
    sum=0
    flag=0
    for j in range(1,n+1):
        if j==n:
            j=0
        if cost[i[j-1]][i[j]]==0:
            flag=1
            break
        sum+=cost[i[j-1]][i[j]]
    if flag==1:
        continue
    ans=min(ans,sum)

print(ans)