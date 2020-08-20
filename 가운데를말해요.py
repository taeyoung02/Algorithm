import sys
# 왼쪽은 최대힙, 오른쪽은 최소힙인 트리의 root노드는 중간값이됨
class heap:
    def __init__(self):
        self.n = int(input())
        self.minarr = [10001]*(self.n//2+2)
        self.maxarr = [10001]*(self.n//2+3)
        self.mincount=0
        self.maxcount=0
        
        self.start()
                
            
    # 그냥 부모보다 작으면 자식으로 박는다
    def insertmin(self,num):
        self.mincount+=1
        i=self.mincount
    
        while i//2>0:
            if self.minarr[i//2]>num:
                self.minarr[i]  = self.minarr[i//2]
                i//=2
            else:
                break
        self.minarr[i]=num

        if self.maxarr[1]>self.minarr[1]:
            self.maxarr[1], self.minarr[1]= self.minarr[1],self.maxarr[1]

            # 바뀐 maxarr[1]이 최대힙에서 최댓값이 아닐경우
            cur=1
            child=2
            temp=self.maxarr[1]
            while child<=self.maxcount:
                if child+1<=self.maxcount:
                    if self.maxarr[child+1]>self.maxarr[child]:
                        child+=1
                
                if temp>=self.maxarr[child]:
                    break
                else:
                    self.maxarr[cur]=self.maxarr[child]
                    self.maxarr[child]=temp
                    cur=child
                    child*=2

            # 바뀐 minarr[1]이 최소힙에서 최소값이 아닐경우
            cur=1
            child=2
            temp=self.minarr[1]
            while child<=self.mincount:
                if child+1<=self.mincount: 
                    if self.minarr[child+1]<self.minarr[child]:
                        child+=1
                if temp<=self.minarr[child]:
                    break
                else:
                    self.minarr[cur]=self.minarr[child]
                    self.minarr[child]=temp
                    cur=child
                    child*=2         
            
    # 그냥 부모보다 작으면 자식으로 박는다
    def insertmax(self,num):
        self.maxcount+=1
        i=self.maxcount
    
        while i//2>0:
            if self.maxarr[i//2]<num:
                self.maxarr[i]  = self.maxarr[i//2]
                i//=2
            else:
                break
        self.maxarr[i]=num

        if self.maxarr[1]>self.minarr[1]:
            self.maxarr[1], self.minarr[1]= self.minarr[1],self.maxarr[1]

            # 바뀐 maxarr[1]이 최대힙에서 최댓값이 아닐경우
            cur=1
            child=2
            temp=self.maxarr[1]
            while child<=self.maxcount:
                if child+1<=self.maxcount:
                    if self.maxarr[child+1]>self.maxarr[child]:
                        child+=1
                
                if temp>=self.maxarr[child]:
                    break
                else:
                    self.maxarr[cur]=self.maxarr[child]
                    self.maxarr[child]=temp
                    cur=child
                    child*=2

            # 바뀐 minarr[1]이 최소힙에서 최소값이 아닐경우
            cur=1
            child=2
            temp=self.minarr[1]
            while child<=self.mincount:
                if child+1<=self.mincount: 
                    if self.minarr[child+1]<self.minarr[child]:
                        child+=1
                if temp<=self.minarr[child]:
                    break
                else:
                    self.minarr[cur]=self.minarr[child]
                    self.minarr[child]=temp
                    cur=child
                    child*=2
 
        
    


    def start(self):
        for k in range(self.n):
            a=int(sys.stdin.readline())
            if k%2==1:
                self.insertmin(a)
            else:
                self.insertmax(a)

            print(self.maxarr[1])
            print(self.maxarr, self.minarr)
            
            
if __name__ == "__main__":
    heap()