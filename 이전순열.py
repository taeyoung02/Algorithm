# from itertools import permutations
# n=int(input())
# arr=list(map(int, input().split()))


# permu=sorted(arr)
# permu=list(permutations(permu))#permutation(리스트) 모든 순열을 오브젝트 형태로 저장
# if permu.index(tuple(arr))==0:
#     print(-1)
#     exit(0)
# ans=permu[permu.index(tuple(arr))-1]
# for i in ans:
#     print(i,end=' ')


def prev_permutation(a):
    """Generate the lexicographically next permutation inplace.

    https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    Return false if there is no next permutation.
    """
    # Find the largest index i such that a[i] < a[i + 1]. If no such
    # index exists, the permutation is the last permutation
    for i in reversed(range(len(a) - 1)):
        if a[i] > a[i + 1]:
            break  # found
    else:  # no break: not found
        return -1  # no next permutation

    # Find the largest index j greater than i such that a[i] < a[j]
    j = next(j for j in reversed(range(i + 1, len(a))) if a[i] > a[j])

    # Swap the value of a[i] with that of a[j]
    a[i], a[j] = a[j], a[i]

    # Reverse sequence from a[i + 1] up to and including the final element a[n]
    a[i + 1:] = reversed(a[i + 1:])
    return a


n=int(input())
arr=list(map(int, input().split()))

res=prev_permutation(arr)
if res==-1:
    print(-1)
    exit(0)
for i in res:
    print(i, end=' ')