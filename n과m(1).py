#1
n,m=map(int,input().split())
check=[0]*10
arr=[]
def BT(arr, n,m,index):
    if index==m:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(1,n+1):
        if check[i]==0:
            arr.append(i)
            check[i]=1
            BT(arr, n, m, index+1)
            arr.pop()
            check[i]=0

BT(arr,n,m,0)

#2
n,m=map(int,input().split())
check=[0]*10
arr=[]
def BT(arr, n,m,index,cur):
    if index==m:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(cur,n+1):
        if check[i]==0:
            arr.append(i)
            check[i]=1
            BT(arr, n, m, index+1, i+1)
            arr.pop()
            check[i]=0

BT(arr,n,m,0,1)

#3
n,m=map(int,input().split())
arr=[]
def BT(arr, n,m, index):
    if index==m:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(1,n+1):
        arr.append(i)
        BT(arr, n, m, index+1)
        arr.pop()


BT(arr,n,m,0)

#4
n,m=map(int,input().split())
arr=[]
def BT(arr, n,m,index,cur):
    if index==m:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(cur,n+1):
        arr.append(i)
        BT(arr, n, m, index+1, i)
        arr.pop()

BT(arr,n,m,0,1)

#5
n,m=map(int,input().split())
num=list(map(int, input().split()))
num.sort()
check=[0]*10
arr=[]
def BT(arr, n,m,index):
    if index==m:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(n):
        if check[i]==0:
            arr.append(num[i])
            check[i]=1
            BT(arr, n, m, index+1)
            arr.pop()
            check[i]=0

BT(arr,n,m,0)

#6
n,m=map(int,input().split())
num=list(map(int, input().split()))
num.sort()
check=[0]*10
arr=[]
def BT(arr, n,m,index,cur):
    if index==m:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(cur,n):
        if check[i]==0:
            arr.append(num[i])
            check[i]=1
            BT(arr, n, m, index+1,i+1)
            arr.pop()
            check[i]=0

BT(arr,n,m,0,0)

#7
n,m=map(int,input().split())
num=list(map(int, input().split()))
num.sort()
arr=[]
def BT(arr, n,m,index):
    if index==m:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(n):
        arr.append(num[i])
        BT(arr, n, m, index+1)
        arr.pop()

BT(arr,n,m,0)

#8
n,m=map(int,input().split())
num=list(map(int, input().split()))
num.sort()
arr=[]
def BT(arr, n,m,index,cur):
    if index==m:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(cur,n):
        arr.append(num[i])
        BT(arr, n, m, index+1,i)
        arr.pop()
BT(arr,n,m,0,0)

#9
n,m=map(int,input().split())
num=list(map(int, input().split()))
check=[0]*10
num.sort()
arr=[]
ans={}
def BT(arr, n,m,index):
    if index==m:
        ans[tuple(arr)]=1
        return

    for i in range(n):
        if check[i]==0:
            arr.append(num[i])
            check[i]=1
            BT(arr, n, m, index+1)
            check[i]=0
            arr.pop()
BT(arr,n,m,0)

keys=list(ans.keys())
for i in keys:
    i=str(i)[1:-1].split(',')
    for j in i:
        print(j,end='')
    print()

#10
n,m=map(int,input().split())
num=list(map(int, input().split()))
check=[0]*10
num.sort()
arr=[]
ans={}
def BT(arr, n,m,index,cur):
    if index==m:
        ans[tuple(arr)]=1
        return

    for i in range(cur,n):
        if check[i]==0:
            arr.append(num[i])
            check[i]=1
            BT(arr, n, m, index+1,i+1)
            check[i]=0
            arr.pop()
BT(arr,n,m,0,0)

keys=list(ans.keys())
for i in keys:
    i=str(i)[1:-1].split(',')
    for j in i:
        print(j,end='')
    print()

#11
n,m=map(int,input().split())
num=list(map(int, input().split()))
num.sort()
arr=[]
ans={}
def BT(arr, n,m,index):
    if index==m:
        ans[tuple(arr)]=1
        return

    for i in range(n):
            arr.append(num[i])
            BT(arr, n, m, index+1)
            arr.pop()
BT(arr,n,m,0)

keys=list(ans.keys())
for i in keys:
    i=str(i)[1:-1].split(',')
    for j in i:
        print(j,end='')
    print()

#12
n,m=map(int,input().split())
num=list(map(int, input().split()))
num.sort()
arr=[]
ans={}
def BT(arr, n,m,index,cur):
    if index==m:
        ans[tuple(arr)]=1
        return

    for i in range(cur,n):
            arr.append(num[i])
            BT(arr, n, m, index+1,i)
            arr.pop()
BT(arr,n,m,0,0)

keys=list(ans.keys())
for i in keys:
    i=str(i)[1:-1].split(',')
    for j in i:
        print(j,end='')
    print()