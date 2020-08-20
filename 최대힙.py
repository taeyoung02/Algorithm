import sys

class heap:
    def __init__(self):
        self.n = int(input())
        self.arr = [0]*(self.n+2)
        self.count=0
        
        self.start()

    def heapmax(self):
        if self.count==0:
            print(0)
        else:
            print(self.arr[1])
            self.arr[1]=self.arr[self.count]
            temp=self.arr[1]
            self.count-=1
            cur=1
            child=2
            while child<=self.count:
                if child+1<=self.count: # 순서가 꼬였어도 자식중에 큰놈이랑
                    # 바꾸기 때문에 자연스럽게 맞춰짐
                    # 루트노드가 오른쪽을 선택하면 왼쪽전체는 무조건 다음루트노드보다
                    # 작은숫자고, 오른쪽의 가장큰숫자가 루트노드 오른쪽으로 온다
                    if self.arr[child+1]>self.arr[child]:
                        child+=1
                if temp>=self.arr[child]:
                    break
                else:
                    self.arr[cur]=self.arr[child]
                    cur=child
                    child*=2
            
            self.arr[cur] = temp
        
                
            
    # 그냥 부모보다 작으면 자식으로 박는다
    def insert(self,num):
        self.count+=1
        i=self.count
    
        while i//2>0:
            if self.arr[i//2]<num:
                self.arr[i]  = self.arr[i//2]
                i//=2
            else:
                break
        self.arr[i]=num       
    


    def start(self):
        for k in range(self.n):
            a=int(sys.stdin.readline())
            if a==0:
                self.heapmax()
            else:
                self.insert(a)
            print(self.arr)
if __name__ == "__main__":
    h=heap()