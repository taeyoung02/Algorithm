n=int(input())
arr=list(map(int,input().split()))

increase=[1]*n
decrease=[1]*n

for i in range(n):
    for j in range(i):
        if (arr[i]>arr[j]) and (increase[i]<increase[j]+1):
            increase[i]=increase[j]+1

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if (arr[i]>arr[j]) and (decrease[i]<decrease[j]+1):
            decrease[i]=decrease[j]+1

res=[0]*n
for i in range(n):
    res[i]=increase[i]+decrease[i]

print(max(res)-1)