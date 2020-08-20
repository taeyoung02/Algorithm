import sys

R,C,M = map(int,input().split())

shark= [list(map(int, sys.stdin.readline().strip().split())) for i in range(0, M)]

# r c 속력 이동방향 크기

ans=0

for i in range(C):
    minR=100000
    K=-1
    for k in range(M):
        if shark[k][1] == i+1 and shark[k][4]!=0:
            if minR>shark[k][0]:
                minR = shark[k][0]
                K=k

    if K!=-1:
        ans+=shark[K][4]
        shark[K][4]=0

    cage = {}
    for k in range(M):
        r = shark[k][0]
        c = shark[k][1]
        s = shark[k][2]
        d = shark[k][3]
        z = shark[k][4]
        
        if z != 0 :
            if d == 1 or d == 2: 
                s = s % ((R-1)*2)
                if d==1:
                    if r-1<s:
                        d=2
                        r=s-r+2
                        if r>R:
                            r=2*R-r
                            d=1
                    else:
                        r-=s
                
                elif d==2:
                    if R-r<s:
                        d=1
                        r=2*R-s-r
                        if r<1:
                            r=1+(1-r)
                            d=2
                    else:
                        r+=s
    
            
            elif d == 3 or d == 4:
                s = s % ((C-1)*2)
                if d==4:
                    if c-1<s:
                        d=3
                        c=s-c+2
                        if c>C:
                            c=2*C-c
                            d=4
                    else:
                        c-=s
                
                elif d==3:
                    if C-c<s:
                        d=4
                        c=2*C-s-c
                        if c<1:
                            c=1+(1-c)
                            d=3
                    else:
                        c+=s
                       
            try:
                if cage[(r,c)][1]<z:
                    shark[ cage[(r,c)][0] ][4]=0
                    cage[(r,c)]=(k,z)
                    shark[k][4]=z
                elif cage[(r,c)][1]>=z:
                    shark[k][4]=0
            except:
                cage[(r,c)]=(k,z)

            shark[k][0]=r
            shark[k][1]=c
            shark[k][3]=d
  


print(ans)