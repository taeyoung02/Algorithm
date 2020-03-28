n= int(input())
arr=list(map(int,input().split()))
j=-1
for i in range(n-1,0,-1):
    if arr[i-1]<arr[i]:
        j=i-1
        break

if j==-1:
    print(-1)
    exit(0)

for i in range(j+1,n):
    if arr[j]<arr[i]:
        k=i
    else:
        break

arr[k],arr[j]=arr[j],arr[k]

for i in range(j+1,n):
    if n-i+j>i:
        arr[i],arr[n-i+j]=arr[n-i+j],arr[i]
for i in arr:
    print(i, end=' ')

    
def next_permutation(a):
    """Generate the lexicographically next permutation inplace.

    https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    Return false if there is no next permutation.
    """
    # Find the largest index i such that a[i] < a[i + 1]. If no such
    # index exists, the permutation is the last permutation
    for i in reversed(range(len(a) - 1)):
        if a[i] < a[i + 1]:
            break  # found
    else:  # no break: not found
        return False  # no next permutation

    # Find the largest index j greater than i such that a[i] < a[j]
    j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])

    # Swap the value of a[i] with that of a[j]
    a[i], a[j] = a[j], a[i]

    # Reverse sequence from a[i + 1] up to and including the final element a[n]
    a[i + 1:] = reversed(a[i + 1:])
    return True

