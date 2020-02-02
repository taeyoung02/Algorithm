n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))

A.sort()
def divide(A,start,end,target):
    mid=int((start+end)/2)
    if start>end:
        return 0
    if A[mid]==target:
        return 1
    if A[mid]>target:
        return divide(A,start,mid-1,target)#리턴하는 습관을 기르자
    else:
        return divide(A,mid+1,end,target)#함수를 리턴안해주면 값이 전달이안됨
for i in range(m):
    print(divide(A,0,n-1,B[i]))
