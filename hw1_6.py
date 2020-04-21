class pattern:
    def __init__(self):
        self.n=int(input())
        self.arr=''
        self.ans=[]

    def pattern(self):
        for _ in range(self.n):
            self.arr=input()
            self.arr=re.sub('100+1+','',self.arr)
            self.arr=re.sub('01','',self.arr)
            if self.arr=='':
                self.ans.append('DANGER')
            else:
                self.ans.append('PASS')
        for i in range(len(self.ans)):
            print(self.ans[i])

if __name__=='__main__':
    import re
    Pattern=pattern()
    Pattern.pattern()
