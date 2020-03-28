def go(arr,index,six,k,cur):
        if index==six:
            for i in arr:
                print(i, end=' ')
            print()
            return
        
        for i in range(cur,k):
            if check[i]==0:
                arr.append(s[i])
                check[i]=1
                go(arr,index+1,six,k,i+1)
                check[i]=0
                arr.pop()

while True:
    inputs = list(map(int,input().split()))
    k,s=inputs[0],inputs[1:]
    check=[0]*k
    arr=[]
    if k==0:
        exit(0)
    
    go(arr,0,6,k,0)
    print()
   
    
