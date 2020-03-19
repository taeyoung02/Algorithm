goal=int(input())
broken_NUM=int(input())
if broken_NUM==0:
    print(min(abs(100-goal), len(str(goal) )))
    exit(0)
broken=list(map(int, input().split()))
ans=abs(goal-100)
for i in range(1000001):
    curr=str(i)
    flag=1
    for k in range(len(curr)):
        if int(curr[k]) in broken:
            flag=0
            break
    if flag==0:
        continue

    ans=min(ans,abs(goal-i)+len(curr))

print(ans)