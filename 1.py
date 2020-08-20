cur=1
child=2
while child<=self.mincount:
    if child+1<=self.mincount: # 순서가 꼬였어도 자식중에 큰놈이랑
        # 바꾸기 때문에 자연스럽게 맞춰짐
        # 루트노드가 오른쪽을 선택하면 왼쪽전체는 무조건 다음루트노드보다
        # 작은숫자고, 오른쪽의 가장큰숫자가 루트노드 오른쪽으로 온다
        if self.minarr[child+1]<self.minarr[child]:
            child+=1
    if temp<=self.minarr[child]:
        break
    else:
        self.minarr[cur]=self.minarr[child]
        cur=child
        child*=2