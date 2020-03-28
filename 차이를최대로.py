from itertools import permutations
n=int(input())
arr=list(map(int,input().split()))

ans=-10000
permu=list(permutations(arr))#permutation(리스트) 모든 순열을 오브젝트 형태로 저장
for i in permu:
    sum=0
    for j in range(n-1):
        sum+=abs(i[j]-i[j+1])
    ans=max(ans,sum)
print(ans)