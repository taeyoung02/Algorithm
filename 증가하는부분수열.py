n=int(input())
arr=list(map(int,input().split()))

d=[0]*n
v=[0]*n
for i in range(n):
    d[i]=1
    for j in range(i):
        if (arr[i]>arr[j]) and (d[i]<d[j]+1):
            d[i]=d[j]+1
            v[i]=j
Max=0
for i in range(0,len(d)):
    if Max<d[i]:
        Max=d[i]
        index=i

result=[arr[index]]

while True:
    index=v[index]
    result.append(arr[index])
    if index==0:
        break

result.reverse()
print(Max)
for i in range(Max):
    print(result[i], end=' ')
