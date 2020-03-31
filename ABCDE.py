n,m=map(int,input().split())
Adjmat=[[0]*n for i in range(n)]
Adjlist=[[] for i in range(n)]
bridge=[]
for i in range(m):
    From, To = map(int,input().split())
    Adjmat[From][To]=1
    Adjmat[To][From]=1
    Adjlist[To].append(From)
    Adjlist[From].append(To)
    bridge.append((From,To))
    bridge.append((To,From))

for i in range(m*2):
    for j in range(m*2):
        a=bridge[i][0]
        b=bridge[i][1]

        c=bridge[j][0]
        d=bridge[j][1]

        if a==c or a==d or b==c or b==d:
            continue

        if Adjmat[b][c]!=1:
            continue

        for e in Adjlist[d]:
            if e==a or e==b or e==c:
                continue
        
            print('1')
            exit(0)
print('0')