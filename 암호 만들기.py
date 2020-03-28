L, C=map(int,(input().split()))

arr=list(input().split())
arr.sort()
def go(L,cur,cnt,i):
    if L==cnt:
        mo=0
        ja=0
        for j in cur:
            if j in ['a','e','i','o','u']:
                mo+=1
            else:
                ja+=1
        if mo>0 and ja>1:
            for j in cur:
                print(j,end='')
            print()
        return
    if C-cnt<L-len(cur) or i>=C:
        return
    go(L,cur+arr[i:i+1],cnt+1,i+1)
    go(L,cur,cnt,i+1)

go(L,[],0,0)
