from itertools import permutations
n=int(input())
arr=[i for i in range(1,n+1)]


permu=list(permutations(arr))#permutation(리스트) 모든 순열을 오브젝트 형태로 저장
for i in permu:
    for j in i:
        print(j, end=' ')
    print()