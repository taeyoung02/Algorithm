import sys
n=int(input())
s=0
arr=[]
for i in range(n):
    order=sys.stdin.readline().strip()#strip안하면 줄바꿈까지 포함됨
    if order[0]!='e' and order[1]!='l':
        order,x=order.split()
        x=int(x)-1
    if order=='add':
        s|=(1<<x)
    if order=='remove':
        s&=~(1<<x)
    if order=='check':
        if s&(1<<x):
            print('1')
        else:
            print('0')
    if order=='toggle':
        if s&(1<<x):
            s=(s&~(1<<x))
        else:
            s|=(1<<x)
    if order=='all':
        s=(1<<20)-1
    if order=='empty':
        s&=0


