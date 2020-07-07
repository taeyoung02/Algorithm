import sys
flag=0
n,m=map(int,input().split())
tree=list(map(int,sys.stdin.readline().strip().split()))


def cutter(low,high):
    h=0
    global flag
    if high>=low:
        mid = (low+high)//2
        for i in range(n):
            if tree[i]>mid:
                h+=(tree[i]-mid)
        if h>m:
            flag=max(mid,flag)
            return cutter(mid+1,high)
        elif h==m:
            print(mid)
            flag=-1
            return
        else:
            return cutter(low,mid-1)

cutter(0,max(tree)-1)
if flag!=-1:
    print(flag)