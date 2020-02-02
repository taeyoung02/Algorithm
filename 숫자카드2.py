import sys
n=int(sys.stdin.readline().rstrip())
A=list(map(int,sys.stdin.readline().rstrip().split()))
m=int(sys.stdin.readline().rstrip())
B=list(map(int,sys.stdin.readline().rstrip().split()))
A.sort()
#lowerbound 찾고자 하는 값 이상이 처음 나타난 위치
#upperbound 찾고자 하는 값 보다 큰값이 처음 나타난 위치
def lowdivide(target):
    start=0
    end=n-1
    while start<end:
        mid=int((start+end)/2)
        if A[mid]<target:
            start = mid+1
        else:
            end=mid
    return end

def upperdivide(target):
    start=0
    end=n-1
    while start<end:
        mid=int((start+end)/2)
        if A[mid]<=target:
            start=mid+1
        else:
            end=mid
    return end

for i in B:
    upper=upperdivide(i)
    low=lowdivide(i)
    if A[upper]==i:
        upper+=1
    print(upper-low,end=' ')

