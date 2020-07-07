n,k=map(int,input().split())
home=[]
for i in range(n):
    home.append(int(input()))

home.sort()
low=1
high=home[n-1]-home[0]

flag=0
while low <= high:
    gap=(low+high)//2
    visit=home[0]
    wifi=1
    for i in range(1,n):
        home[i]-visit
        if home[i]-visit >= gap:
            wifi+=1
            visit=home[i]
    
    if wifi>=k:
        low=gap+1
        ans=gap
    elif wifi<k:
        high=gap-1
    

print(ans)