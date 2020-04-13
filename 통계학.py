from sys import stdin
n=int(stdin.readline().strip())
arr=[]
for i in range(n):
    arr.append(int(stdin.readline().strip()))

arr.sort()
print(round(sum(arr)/len(arr)))
print(arr[len(arr)//2])
Dict=dict()
Max=0
for i in range(n):
    try:
        Dict[arr[i]]+=1
    except:
        Dict[arr[i]]=1
    Max=max(Max,Dict[arr[i]])
choibin=[]
for key,value in Dict.items():
    if value==Max:
        choibin.append(key)
choibin.sort()
if len(choibin)==1:
    print(choibin[0])
else: print(choibin[1])
print(max(arr)-min(arr))